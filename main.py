#
#
#
#
import subprocess
import sys
import os
import argparse


# string return class
class StringCreator:
    def __init__(self):
        pass;

    @staticmethod
    def ConfigString():
        with open('../content/ConfigIndexContent.js', 'r') as f:
            content = f.read();
            f.close();
        return content;
        
     
    @staticmethod    
    def IndexString():
        with open('../content/IndexContent.js', 'r') as f:
            content = f.read();
            f.close();
        return content;
    @staticmethod
    def UtilIndexString():
        with open('../content/UtilIndexContent.js', 'r') as f:
            content = f.read();
            f.close();
        return content;
    
    @staticmethod
    def UtilCommonErrorString():
        with open('../content/CommonErrorContent.js', 'r') as f:
            content = f.read();
            f.close();
        return content;
    
    @staticmethod
    def UtilFormatDataString():
        with open('../content/UtilFormatDataContent.js', 'r') as f:
            content = f.read();
            f.close();
        return content;
    
    @staticmethod
    def ExpressAppString():
        with open('../content/ExpressAppContent.js', 'r') as f:
            content = f.read();
            f.close();
        return content;


# directory class
class Direcatory:
    def __init__(self, parent_dir='./'):
        self.parent_dir = parent_dir
        self.project_dir = None

    # make the project dir in the parent directory
    def createProject(self, project_name):
        if project_name:
            if (os.path.exists(project_name)):
                return True
            os.mkdir(os.path.join(self.parent_dir, project_name))
            return True
        else:
            return False

    def changeDir(self, path_name=None):
        pass
        if path_name:
            os.chdir(os.path.join(self.parent_dir, path_name))
            return True
        return False

    

    # create folder with index file
    def createFolderWithIndexFile(self, folder_name="", index_content=""):
        if(not os.path.exists(f'{folder_name}'.format(folder_name))):
            # folder is not exist
            if(not os.path.exists(f"{folder_name}".format(folder_name))):
                os.makedirs(os.path.join(os.getcwd(), folder_name));

            # create file 
            with open(f"{folder_name}/index.js".format(folder_name), 'w') as f:
                f.write(index_content);
                f.close();
            return True;
        print(f"{folder_name} already exist.".format(folder_name));
        return False;

    # create folder with _@ file name
    def createFolderWithAnyFile(self, folder_name="", file_name=None ,index_content=""):
        if(not os.path.exists(f'{folder_name}/{file_name}'.format(folder_name, file_name))):
            # folder is not exist
            if(not os.path.exists(f"{folder_name}".format(folder_name))):
                os.makedirs(os.path.join(os.getcwd(), folder_name));

            # create file 
            with open(f"{folder_name}/{file_name}".format(folder_name, file_name), 'w') as f:
                f.write(index_content);
                f.close();
            return True;
        print(f"{folder_name}/{file_name} already exist.".format(folder_name, file_name));
        return False;


    

    @staticmethod
    def fileExist(file_name):
        if os.path.exists(file_name):
            return True
        else:
            return False


def main():
    parser = argparse.ArgumentParser()

    # project name
    parser.add_argument('-p', type=str, help="The project folder name.")
    parser.add_argument('--model', type=str, nargs='+',
                        help="The model of the project")
    args = parser.parse_args()
    Dir = Direcatory()
    
    if(args.p):
        Dir.createProject(project_name=args.p)

        # inside the project dir
        Dir.changeDir(args.p)

        if (not Direcatory.fileExist(file_name="package.json")):
            subprocess.run(['sudo', 'yarn', 'init'])
            subprocess.run(['sudo', 'yarn', 'add', 'express',
                       'dotenv', 'cors', 'http-errors', 'body-parser'])
        else:
            print('Already necessary package is installed.')

        # create src
        Dir.createFolderWithIndexFile(folder_name="src/", index_content=StringCreator.IndexString());
        Dir.createFolderWithIndexFile(folder_name="src/api");
        Dir.createFolderWithIndexFile(folder_name="src/config",index_content=StringCreator.ConfigString());
        Dir.createFolderWithIndexFile(folder_name="src/util", index_content=StringCreator.UtilIndexString());
        Dir.createFolderWithAnyFile(folder_name="src/util", file_name="common-error.js", index_content=StringCreator.UtilCommonErrorString());
        Dir.createFolderWithAnyFile(folder_name="src/util", file_name="Format-Data.js", index_content=StringCreator.UtilFormatDataString());
        Dir.createFolderWithAnyFile(folder_name="src/", file_name="express-app.js", index_content=StringCreator.ExpressAppString());
    elif ():
        if(args.model):
            pass;
            
        else:
            print("No model exist here.");
        print('No project name found.')

    print(args.p, args.model)


if __name__ == "__main__":
    main()
