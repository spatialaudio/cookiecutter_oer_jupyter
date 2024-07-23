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

	if is_git_installed:

		#subprocess.call(['git', 'init'])
		#subprocess.call(['git', 'add', '*'])
		#subprocess.call(['git', 'commit', '-m', 'Initial commit'])
		print('Initialized Git')

	else:
		print('No git installation found - git initialization skipped!')

	if {% if cookiecutter.create_remote_and_push == "Yes" %}True{% else %}False{% endif %}:

		if is_github_cli_installed:

			#subprocess.call(['gh', 'repo', 'create', '--'+{{cookiecutter.git_visibility}}, '--source', '--push'])
			print('Created GitHub remote and pushed local repository')

		else:
			print('No GitHub CLI installation found - GitHub initialization and push local->remote skipped!')

else:
	print('No git initialized')
