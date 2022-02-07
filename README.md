# Download LSUN Dataset in Windows environment
![image](https://user-images.githubusercontent.com/77098071/147448785-967a97dd-9bc0-420b-897c-fe4fb57683ec.png) 
![image](https://user-images.githubusercontent.com/77098071/147448468-87e8c8dd-f57e-4555-a738-2edfbe513e3a.png)

__Please refer to this web page for the code below. :__ https://www.yf.io/p/lsun

Special thanks to my supervisor, Hanhoon Park for revising most of them.

아래의 코드는 주로 Windows를 사용하는 한국인 사양에 맞춰 수정된 LSUN 데이터셋 호출 코드 입니다.   
(Below is the LSUN dataset call code modified to meet the Korean specifications that mainly use Windows.)

## 사용법
__1. LSUN 공식 웹페이지에서 lmdb 파일을 직접 다운받고 data.py가 있는 폴더로 옮겨 줍니다.__   
(download.py를 작동시키는 법은 터득 못해서 직접 다운받았습니다.)   
<hr/>

__2. cmd 창주소를 data.py 파일이 있는 폴더로 이동합니다.__   
```python
python data.py export [lmdb 폴더명] --out_dir [저장하고 싶은 폴더명] --flat
```
예시)
```python
python data.py export church_outdoor_train_lmdb --out_dir train --flat
```
이렇게 하면, mdb 파일이 포함된 "church_outdoor_train_lmdb"폴더를 풀어서 data.py 파일이 있는 폴더에 "train"이름의 폴더를 생성후, webp 형태 이미지로 저장됩니다.

* --flat을 떼면 특정 키폴더에 저장됩니다. --flat을 붙이는 것을 권장합니다.
<hr/>

__3. webp 이미지를 png 이미지로 변환__
```python
python convert.py --indir[webp 이미지 폴더명] --outdir [새로 저장하고 싶은 png 폴더명]
```
예시)
```python
python convert.py --indir church_outdoor_train --outdir church_outdoor_train_png
```
이렇게 하면 webp 형태의 이미지를 png 형태 이미지로 convert하여 저장합니다.
<hr/>

__4. 마지막으로, 저장한 이미지는 resizing.py 파일을 이용해 크기를 통일하실수 있습니다.__




### Citing LSUN

    @article{yu15lsun,
        Author = {Yu, Fisher and Zhang, Yinda and Song, Shuran and Seff, Ari and Xiao, Jianxiong},
        Title = {LSUN: Construction of a Large-scale Image Dataset using Deep Learning with Humans in the Loop},
        Journal = {arXiv preprint arXiv:1506.03365},
        Year = {2015}
    }
