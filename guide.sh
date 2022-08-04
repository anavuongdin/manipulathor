# Step 1 - git clone ManipulaTHOR
git clone https://github.com/allenai/manipulathor.git
pip install gdown

# Step 2 - download prerequisites
cd manipulathor
cd datasets
gdown https://drive.google.com/uc?id=13fOGheELJuoXv_JWRPGcpu2fBY-jKWKB
unzip apnd-dataset.zip

cd ..
cd pretrained_models
gdown https://drive.google.com/uc?id=1axZRgY3oKgATu0zoi1LeLxUtqpIXmJCg
unzip armpointnav_saved_checkpoints.zip

# Step 3 - install libraries
cd ..
pip install -e git+https://github.com/allenai/ai2thor.git@bcc2e62970823667acb5c2a56e809419f1521e52#egg=ai2thor
pip install allenact==0.2.2
pip install allenact-plugins==0.2.2
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt

# Step 4 - copy libraries to venv
## NOTE: may need to modify the destination paths
#cp -R manipulathor_baselines /media/SSD/anvd4/venv/lib/python3.8/site-packages/allenact
#cp -R ithor_arm /media/SSD/anvd4/venv/lib/python3.8/site-packages/allenact
#cp -R manipulathor_utils /media/SSD/anvd4/venv/lib/python3.8/site-packages/allenact
### Before these command lines, create projects.manipulathor_disturb_free
cp -R manipulathor_baselines/armpointnav_baselines /media/SSD/anvd4/venv/lib/python3.8/site-packages/allenact/projects/manipulathor_disturb_free
cp -R manipulathor_plugin /media/SSD/anvd4/venv/lib/python3.8/site-packages/allenact_plugins
cp -R embodiedai/sensors /media/SSD/anvd4/venv/lib/python3.8/site-packages/allenact/embodiedai

# Step 5 - fix paths inside files
sudo env "PATH=$PATH" python /media/SSD/anvd3/manipulathor/scripts/startx.py
## This step needs to be manually handled by modifying in each bug files
## Need to add 'allenact' before each bug files

# Step 6 - Scripts for running training & evaluation
### Table 1
#### Test-SeenObj
allenact allenact/manipulathor_baselines/armpointnav_baselines/experiments/ithor/armpointnav_depth.py -o test_out -s 1 -t test -c pretrained_models/saved_checkpoints/depth_armpointnav.pt
#### Test-NovelObj
allenact allenact/manipulathor_baselines/armpointnav_baselines/experiments/ithor/test_NovelObj_armpointnav_depth -o test_out -s 1 -t test -c pretrained_models/saved_checkpoints/depth_armpointnav.pt
#### SeenScenes-NovelObj
allenact allenact/manipulathor_baselines/armpointnav_baselines/experiments/ithor/test_SeenScenes_NovelObj_armpointnav_depth -o test_out -s 1 -t test -c pretrained_models/saved_checkpoints/depth_armpointnav.pt

### Table 2
#### No-Vision
allenact allenact/manipulathor_baselines/armpointnav_baselines/experiments/ithor/armpointnav_no_vision -o test_out -s 1 -t test -c pretrained_models/saved_checkpoints/no_vision_armpointnav.pt
#### Disjoint Model
allenact allenact/manipulathor_baselines/armpointnav_baselines/experiments/ithor/armpointnav_disjoint_depth -o test_out -s 1 -t test -c pretrained_models/saved_checkpoints/disjoint_model_armpointnav.pt
#### RGB Model
allenact allenact/manipulathor_baselines/armpointnav_baselines/experiments/ithor/armpointnav_rgb -o test_out -s 1 -t test -c pretrained_models/saved_checkpoints/rgb_armpointnav.pt
#### RGB-Depth Model
allenact allenact/manipulathor_baselines/armpointnav_baselines/experiments/ithor/armpointnav_rgbdepth -o test_out -s 1 -t test -c pretrained_models/saved_checkpoints/rgbdepth_armpointnav.pt
#### Depth Model
allenact allenact/projects/manipulathor_disturb_free/armpointnav_baselines/experiments/ithor/armpointnav_depth -o test_out -s 1 -t test -cpretrained_models/saved_checkpoints/depth_armpointnav.pt

