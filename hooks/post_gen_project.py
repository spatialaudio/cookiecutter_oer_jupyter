import subprocess

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
