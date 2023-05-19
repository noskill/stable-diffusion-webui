from launch import prepare_environment
from modules.shared import cmd_opts
from modules import extensions
from webui import initialize
import sys


if __name__ == '__main__':
    prepare_environment()
    initialize()
    extensions.list_extensions()
    sys.path.append('extensions/SD-CN-Animation/scripts/core/')
    sys.path.append('extensions/SD-CN-Animation/')
    import vid2vid
    args = cmd_opts
    args_dict = dict()
    args_dict['file'] = args.input
    args_dict['height'] = args.height
    args_dict['width'] = args.width
    args_dict['save_frames_check'] = False
    args_dict['output_path'] = args.output
    args_dict['script_inputs'] = []
    args_dict['mode'] = 0 # inpaint or img2img
    args_dict['override_settings'] = []
    args_dict['processing_strength'] = args.processing_strength
    args_dict['denoising_strength'] = args.denoising_strength
    args_dict['prompt'] = args.prompt
    args_dict['n_prompt'] = args.negative_prompt
    args_dict['prompt_styles'] = []
    args_dict['seed'] = args.seed
    args_dict['sampler'] = args.sampler
    args_dict['sampling_steps'] = args.sampling_steps
    args_dict['script_inputs'] = [0]
    args_dict['occlusion_mask_flow_multiplier'] = 5 
    args_dict['occlusion_mask_difo_multiplier'] = 2 
    args_dict['occlusion_mask_difs_multiplier'] = 0
    args_dict['occlusion_mask_blur'] = 3
    args_dict['step_1_processing_mode'] = 0
    args_dict['step_1_blend_alpha'] = 1
    args_dict['step_1_seed'] = args_dict['seed']
    args_dict['step_2_seed'] = args_dict['seed']
    args_dict['occlusion_mask_trailing'] = True
    args_dict['output'] = args.output 

    i = 0
    for x in vid2vid.start_process_no_gui(**args_dict):
        i += 1
