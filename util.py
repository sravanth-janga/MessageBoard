from genericpath import isdir
import os,sys
import argparse
import config.settings as st
ops = {'1':'static','2':'templates'}
def main():
    parser = argparse.ArgumentParser(description='Django utility script')
    parser.add_argument("type",default='1',choices=['1','2'],
                help="specify the type of file you want to create")

    parser.add_argument('fname',help="specify the file name you want to add")
    args = parser.parse_args()
    if(args.type=='1'):
        flist = args.fname.split(os.sep)
        dest = ''
        if(len(flist)==1):
            fname=flist[0]
        else:
            fname=flist[1]
            dest = flist[0]

        dest = os.path.join(st.STATICFILES_DIRS[0],dest)
        print(f"Creating the file/files {fname} in {dest} ")
        sub = fname.split(".")[-1]
        if(sub not in ["css","js"]):
            print("please specify valid extension (css or js)")
            sys.exit(1)
        root = os.path.join(dest,sub)
        if(not os.path.isdir(root)):
            os.mkdir(root)
        with open(os.path.join(root,fname),'w') as f:
            pass
        print("done ✅️")
    if(args.type=='2'):
        flist = args.fname.split(os.sep)
        dest = ''
        if(len(flist)==1):
            fname=flist[0]
        else:
            fname=flist[1]
            dest = flist[0]

        dest = os.path.join(st.TEMPLATES[0]['DIRS'][0],dest)
        print(f"Creating the file/files {fname} in {dest} ")
        if(fname.split(".")[-1]!="html"):
            print("template name should have html extension!")
            sys.exit(1)
        if(not os.path.isdir(dest)):
            os.mkdir(dest)
        with open(os.path.join(dest,fname),'w') as f:
            pass
        print("done ✅️")
if __name__=='__main__':
    main()
