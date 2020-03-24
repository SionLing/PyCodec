# Do H.264 core encoding process
import prediction
import matplotlib.pyplot as plt
import numpy as np
from numpy import r_
import transform as tf
import coding as cd
from bitstring import BitStream, BitArray
import NaluStreamer as ns
from h26x_extractor import nalutypes

def encoding16x16(block):
    """
    Encode a 16x16 macroblock
    Args:
        block: 16x16 matrix block
    
    Returns:
        encoding of current macroblock
    """
    QP = 6
    size = block.shape
    step = 4

    result = BitStream()

    # step1: 4x4 transform, quantization and coding
    current = np.full((step, step), 0)
    for i in r_[:size[0]:step]:
        for j in r_[:size[1]:step]:

            current = block[i:(i+step), j:(j+step)]
            print("current block:")
            print(current)

            temp = tf.forwardTransformAndScaling4x4(current, QP)
            print("coefficients:")
            print(temp)
            ac_code = cd.CAVLC(temp)
            result.append(ac_code)

    # step2: Get the DC element of each 4x4 block
    DC_block = np.full((step, step), 0)
    for i in r_[:size[0]:step]:
        for j in r_[:size[1]:step]:
            x = int(i/step)
            y = int(j/step)
            DC_block[x][y] = block[i, j]
    
    # DC transorm coding
    dc_trans = tf.forwardHadamardAndScaling4x4(DC_block, QP)
    dc_code = cd.CAVLC(dc_trans)
    result.append(dc_code)

    return result

def encode(im):
    """
    The core process of H264 encoding
    Args:
        im: the input frame

    returns:
        The binary code of the frame
    """

    predict, residual, mode_map = prediction.IntraPrediction(im, 16)  # 16x16 intra mode

    #according to page 133 Figure 8-6
    totalMacro = BitStream()
    step = 16
    imsize = residual.shape
    for i in r_[:imsize[0]:step]:
        for j in r_[:imsize[1]:step]:

            block16x16 = residual[i:(i+step), j:(j+step)]
            macro = encoding16x16(block16x16)

            I_16x16_2_0_1 = 15   #temp code, TODO: should add some basic prediction type in nalutypes
            mb = ns.MacroblockLayer(I_16x16_2_0_1)
            mb.set__residual(residual)

            totalMacro.append(macro)

    return totalMacro

def main():
    """
    work on a keyframe, can just encode one keyframe right now
    """
    # step1, open the file
    f = "E:/temp/output/nalustreamer.264"
    handler = ns.openNaluFile(f)

    # step2, generate sps & pps
    sps = ns.SpsStreamer(nalutypes.NAL_UNIT_TYPE_SPS)
    sps.set__profile_idc(66) # Baseline profile
    sps.set__level_idc(3) # level 3
    sps.set__seq_parameter_set_id(0)
    sps.set__log2_max_frame_num_minus4(0)
    sps.set__pic_order_cnt_type(0)
    sps.set__num_ref_frames(2)
    sps.set__gaps_in_frame_num_value_allowed_flag(False)
    sps.set__pic_width_in_mbs_minus_1(512)
    sps.set__pic_height_in_map_units_minus1(512)
    sps.set__frame_mbs_only_flag(True)
    sps.set__direct_8x8_inference_flag(True)
    sps.set__frame_cropping_flag(False)
    sps.set__vui_parameters_present_flag(False)
    sps.export(handler)

    pps = ns.PpsStreamer(nalutypes.NAL_UNIT_TYPE_PPS)
    pps.export(handler)

    # step3, write a key frame
    frame = ns.SliceHeader(nalutypes.NAL_UNIT_TYPE_CODED_SLICE_IDR)  # TODO: slice type shoud be defined
    print(sps.log2_max_frame_num_minus4)
    temp = sps.get__log2_max_frame_num_minus4()
    frame.set__frame_num(temp, 0)
    
    frame.export(handler)

    # step4, write slice data
    im = plt.imread("E:/liumangxuxu/code/PyCodec/modules/lena2.tif").astype(float)
    residual = encode(im)   # currently we just support 16x16 prediction
    code = ns.SliceData()
    code.set__macroblock_layer(residual)

    # step5, close the file
    ns.closeNaluFile(handler)

if __name__ == '__main__':
    main()
    