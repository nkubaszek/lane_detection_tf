from easydict import EasyDict as edict

__C = edict()
# Consumers can get config by: from config import cfg

cfg = __C

# Train options
__C.TRAIN = edict()

# Set the shadownet training epochs
# Original
__C.TRAIN.EPOCHS =500010
# Train testing on 6 images
#__C.TRAIN.EPOCHS = 2200
# Set the display step
__C.TRAIN.DISPLAY_STEP = 1
# Set the test display step during training process
__C.TRAIN.TEST_DISPLAY_STEP = 1000
# Set the momentum parameter of the optimizer
__C.TRAIN.MOMENTUM = 0.9
# Set the initial learning rate
#__C.TRAIN.LEARNING_RATE = 0.0005	# Orig
__C.TRAIN.LEARNING_RATE = 0.0004
# Set the GPU resource used during training process
#__C.TRAIN.GPU_MEMORY_FRACTION = 0.85	# Original
__C.TRAIN.GPU_MEMORY_FRACTION = 0.90
# Set the GPU allow growth parameter during tensorflow training process
__C.TRAIN.TF_ALLOW_GROWTH = False
# Set the shadownet training batch size
__C.TRAIN.BATCH_SIZE = 2	#8 Orig

# Set the shadownet validation batch size
__C.TRAIN.VAL_BATCH_SIZE = 2
# Set the learning rate decay steps
__C.TRAIN.LR_DECAY_STEPS = 410000
# Set the learning rate decay rate
__C.TRAIN.LR_DECAY_RATE = 0.1
# Set the class numbers
__C.TRAIN.CLASSES_NUMS = 2
# Set the image height
__C.TRAIN.IMG_HEIGHT = 256
# Set the image width
__C.TRAIN.IMG_WIDTH = 512

# Test options
__C.TEST = edict()

# Set the GPU resource used during testing process
__C.TEST.GPU_MEMORY_FRACTION = 0.8
# Set the GPU allow growth parameter during tensorflow testing process
__C.TEST.TF_ALLOW_GROWTH = True
# Set the test batch size
__C.TEST.BATCH_SIZE = 8