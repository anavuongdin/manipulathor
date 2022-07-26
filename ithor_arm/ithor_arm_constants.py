"""Constant values and hyperparameters that are used by the environment."""
import ai2thor
import ai2thor.fifo_server
from allenact_plugins.ithor_plugin.ithor_environment import IThorEnvironment

# MANIPULATHOR_COMMIT_ID = "68212159d78aab5c611b7f16338380993884a06a"
# MANIPULATHOR_COMMIT_ID = 'bcc2e62970823667acb5c2a56e809419f1521e52'
MANIPULATHOR_COMMIT_ID = "a84dd29471ec2201f583de00257d84fac1a03de2"

MOVE_THR = 0.02
ARM_MIN_HEIGHT = 0.450998873
ARM_MAX_HEIGHT = 1.8009994
MOVE_ARM_CONSTANT = 0.05
MOVE_ARM_HEIGHT_CONSTANT = MOVE_ARM_CONSTANT
CONSTANTLY_MOVING_OBJECTS = {'FloorPlan1':{'Egg|-02.01|+00.81|+01.25', }, 'FloorPlan2':{'Egg|+00.06|+00.97|-00.17', }, 'FloorPlan4':{'Egg|-03.32|+01.31|+02.85', }, 'FloorPlan5':{'Egg|-00.14|+00.78|-01.92', }, 'FloorPlan6':{'Egg|-02.53|+00.60|-00.71', }, 'FloorPlan10':{'Egg|+00.89|+01.16|+01.09', }, 'FloorPlan11':{'Egg|-02.32|+00.80|-01.72', }, 'FloorPlan15':{'Tomato|-02.30|+00.97|+03.69', }, 'FloorPlan16':{'Ladle|+02.61|+01.04|-01.50', }, 'FloorPlan20':{'Vase|+01.50|+00.56|+02.45', }, 'FloorPlan21':{'Lettuce|-00.28|+00.97|+01.13', }, 'FloorPlan22':{'Apple|+00.28|+01.15|+01.58', }, 'FloorPlan23':{'Egg|-00.46|+01.40|-01.01', }, 'FloorPlan24':{'Microwave|-01.53|+01.25|+03.88', }, 'FloorPlan27':{'Ladle|-00.10|+00.95|+02.55', }, 'FloorPlan28':{'Apple|-00.44|+01.00|-01.48', }, 'FloorPlan217':{'Chair|-04.74|+00.01|+04.61', }, 'FloorPlan229':{'Box|-03.42|+00.59|+02.44', }, 'FloorPlan316':{'Pen|+00.14|+00.70|-02.21', 'Pencil|+00.21|+00.70|-02.20', }, 'FloorPlan326':{'BaseballBat|-02.90|+00.06|-02.70', }, 'FloorPlan416':{'ToiletPaper|-01.57|+00.64|+00.05', }, 'FloorPlan418':{'ToiletPaper|-00.37|+00.05|-03.86', }}

ADITIONAL_ARM_ARGS = {
    "disableRendering": True,
    "returnToStart": True,
    "speed": 1,
}

MOVE_AHEAD = "MoveAheadContinuous"
ROTATE_LEFT = "RotateLeftContinuous"
ROTATE_RIGHT = "RotateRightContinuous"
MOVE_ARM_HEIGHT_P = "MoveArmHeightP"
MOVE_ARM_HEIGHT_M = "MoveArmHeightM"
MOVE_ARM_X_P = "MoveArmXP"
MOVE_ARM_X_M = "MoveArmXM"
MOVE_ARM_Y_P = "MoveArmYP"
MOVE_ARM_Y_M = "MoveArmYM"
MOVE_ARM_Z_P = "MoveArmZP"
MOVE_ARM_Z_M = "MoveArmZM"
PICKUP = "PickUpMidLevel"
DONE = "DoneMidLevel"


ENV_ARGS = dict(
    gridSize=0.25,
    width=224,
    height=224,
    visibilityDistance=1.0,
    agentMode="arm",
    fieldOfView=100,
    agentControllerType="mid-level",
    server_class=ai2thor.fifo_server.FifoServer,
    useMassThreshold=True,
    massThreshold=10,
    autoSimulation=False,
    autoSyncTransforms=True,
)

TRAIN_OBJECTS = ["Apple", "Bread", "Tomato", "Lettuce", "Pot", "Mug"]
TEST_OBJECTS = ["Potato", "SoapBottle", "Pan", "Egg", "Spatula", "Cup"]


def make_all_objects_unbreakable(controller):
    all_breakable_objects = [
        o["objectType"]
        for o in controller.last_event.metadata["objects"]
        if o["breakable"] is True
    ]
    all_breakable_objects = set(all_breakable_objects)
    for obj_type in all_breakable_objects:
        controller.step(action="MakeObjectsOfTypeUnbreakable", objectType=obj_type)


def reset_environment_and_additional_commands(controller, scene_name):
    controller.reset(scene_name)
    controller.step(action="MakeAllObjectsMoveable")
    controller.step(action="MakeObjectsStaticKinematicMassThreshold")
    make_all_objects_unbreakable(controller)
    return


def transport_wrapper(controller, target_object, target_location):
    transport_detail = dict(
        action="PlaceObjectAtPoint",
        objectId=target_object,
        position=target_location,
        forceKinematic=True,
    )
    advance_detail = dict(action="AdvancePhysicsStep", simSeconds=1.0)

    if issubclass(type(controller), IThorEnvironment):
        event = controller.step(transport_detail)
        controller.step(advance_detail)
    elif type(controller) == ai2thor.controller.Controller:
        event = controller.step(**transport_detail)
        controller.step(**advance_detail)
    return event


VALID_OBJECT_LIST = [
    "Knife",
    "Bread",
    "Fork",
    "Potato",
    "SoapBottle",
    "Pan",
    "Plate",
    "Tomato",
    "Egg",
    "Pot",
    "Spatula",
    "Cup",
    "Bowl",
    "SaltShaker",
    "PepperShaker",
    "Lettuce",
    "ButterKnife",
    "Apple",
    "DishSponge",
    "Spoon",
    "Mug",
]

import json

with open("datasets/apnd-dataset/starting_pose.json") as f:
    ARM_START_POSITIONS = json.load(f)
