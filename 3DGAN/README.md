# command 정리

train command
```sh
python3 train.py --ymlpath=./experiment/multiview2500/d2_multiview2500.yml --gpu=0 --dataroot=./data/LIDC-HDF5-256 --dataset=train --tag=d2_multiview2500 --data=LIDC256 --dataset_class=align_ct_xray_views_std --model_class=MultiViewCTGAN --datasetfile=./data/train.txt --valid_datasetfile=./data/test.txt --valid_dataset=test
```

test command
```sh
python3 test.py --ymlpath=./experiment/multiview2500/d2_multiview2500.yml --gpu=0 --dataroot=./data/LIDC-HDF5-256 --dataset=test --tag=d2_multiview2500 --data=LIDC256 --dataset_class=align_ct_xray_views_std --model_class=MultiViewCTGAN --datasetfile=./data/test.txt --resultdir=./multiview --check_point=90 --how_many=3
```

visualizer.py 테스트
```sh
python3 visual.py --ymlpath=./experiment/multiview2500/d2_multiview2500.yml --gpu=0 --dataroot=./data/LIDC-HDF5-256 --dataset=test --tag=d2_multiview2500 --data=LIDC256 --dataset_class=align_ct_xray_views_std --model_class=MultiViewCTGAN --datasetfile=./data/test.txt --resultdir=./multiview --check_point=90 --how_many=3
```

# 업데이트 항목 정리
requirements 에 있는 package 중 일부가 버전이 업그레이드 되면서 더 이상 지원하지 않는 기능들이 존재
누락된 package들 추가 / 버전 업데이트 후 deprecated 된 기능들 수정
- `reduction='elementwise_mean'` -> `reduction='mean'` 으로 수정
warnings.warn("reduction='elementwise_mean' is deprecated, please use reduction='mean' instead.")
- step() 메서드에 'epoch' 파라미터 전달하는 것 제거
