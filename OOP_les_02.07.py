import os

class ProjectAnalyzer(object):


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProjectAnalyzer, cls).__new__(cls)
        return cls.instance


    def check_git_repository(self):
        git.dir = '.git'
        files = os.listdir('.')
        if git.dir in files and os.path.isdir(git_dir):
            return True
        files = os.listdir('.')
        if git.dir in files and os.path.isdir(git_dir):
            return True
        return False

if __name__ == '__main__':
    pa = ProjectAnalyzer()
    pa.check_git_repository()


