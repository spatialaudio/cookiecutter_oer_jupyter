import subprocess
import shutil
import os



def check_directory() -> bool:

	cwd = os.getcwd()
	
	if os.path.basename(cwd) == '{{cookiecutter.directory_name}}':
		return True
	else:
		return False

def is_git_installed() -> bool:
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False

def is_github_cli_installed() -> bool:
    try:
        subprocess.run(["gh", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False
    
def delete_in_list(list):
	for del_path in list:
		if os.path.exists(del_path):
			if os.path.isdir(del_path):
				shutil.rmtree(del_path)
			else:
				os.remove(del_path)
				
    

# cleanup
if check_directory():

	# remove unneeded files
	cu_files = ['.ipynb_checkpoints']
	delete_in_list(cu_files)

	# remove ci files if not wanted
	if {% if cookiecutter.include_ci == "No" %}True{% else %}False{% endif %}:
		ci_files = ['.github', 'ci', '.travis.yml']
		delete_in_list(ci_files)
else:
	raise Exception('Wrong working directory!')

# importing notebook collection
if {% if cookiecutter.import_notebooks == "Yes" %}True{% else %}False{% endif %}:

	del_files = ['index.ipynb', 'index.rst', 'requirements.txt', '.DS_Store']
	del_folders = ['introduction','data']
	nb_col_path = '{{cookiecutter.notebook_collection_path}}'
	cwd = os.getcwd()
	nb_col = os.listdir(nb_col_path)

	if check_directory():
		
		# remove placeholder files and folders
		for del_path in del_files:
			if os.path.exists(del_path):
				os.remove(del_path)

		for del_path in del_folders:
			if os.path.exists(del_path):
				shutil.rmtree(del_path)
			
		# copy notebook collection
		for source in nb_col:
			if os.path.isdir(os.path.join(nb_col_path, source)):
				shutil.copytree(os.path.join(nb_col_path, source), os.path.join(cwd, source), dirs_exist_ok=True)
			else:
				shutil.copy2(os.path.join(nb_col_path, source), os.path.join(cwd, source))

	else:
		raise Exception('Wrong working directory!')

if {% if cookiecutter.create_git == "Yes" %}True{% else %}False{% endif %}:

	if is_git_installed():

		subprocess.run(['git', 'init'])
		subprocess.run(['git', 'add', '*'])
		subprocess.run(['git', 'commit', '-m', 'Initial commit'])
		print('Initialized Git')

		if {% if cookiecutter.create_remote_and_push == "Yes" %}True{% else %}False{% endif %}:

			if is_github_cli_installed():

				if '{{cookiecutter.github_organization}}' != 'none' and '{{cookiecutter.github_organization}}' != 'None':
					new_repo = '{{cookiecutter.github_organization}}' +'/'+ '{{cookiecutter.directory_name}}'
				else:
					new_repo = '{{cookiecutter.directory_name}}'

				subprocess.run(['gh', 'repo', 'create', new_repo, '--'+'{{cookiecutter.git_visibility}}', '--source', '.', '--push'])
				print('Created GitHub remote and pushed local repository')

			else:
				print('No GitHub CLI installation found - GitHub initialization and push local->remote skipped!')

		if {% if cookiecutter.push_existing_remote == "Yes" %}True{% else %}False{% endif %}:
				
			if is_github_cli_installed():

				subprocess.run(['git', 'remote', 'add', 'origin', '{{cookiecutter.git_remote}}'])
				subprocess.run(['git', 'push'])
				print('Created GitHub remote and pushed local repository')

			else:
				print('No GitHub CLI installation found - GitHub initialization and push local->remote skipped!')

	else:
		print('No git installation found - git initialization skipped!')

else:
	print('No git initialized')
