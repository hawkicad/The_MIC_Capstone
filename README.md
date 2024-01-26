# The_MIC_Capstone

## Project Goal:

To create a webscraping/API tool that will reduce the amount of navigation users have to do when attempting to fully comprehend any MIC article. This project will aim to gather all the definitions from the glossary page, host them in a db, and be capable of reproducing any given defintion in a popup when a user hovers over it in an article. The current functionality is that a user has the option to click on a word they may not know or want more clarity on. When they do this it will navigate them to the Glossary page where they can find their desired term. Our goal is to remove the need to leave a page to understand what a term means. Additionally, we want the project to be scalable for a furture team to add to.

## How CI/CD flow will work

### There are three environments for our code to live in
- The first being DEV
  - This the branch that we will be merging our code to rather than directly to main
  - This helps to preserve the quality of main (PROD) so we don't introduce smelly or error ridden code
  - It is much easier to find bugs if our code if thoroughly reviewed
- The second being QA
  - This is where the DEV branch will be merged/promoted to
  - This is the branch were rigorous testing occurs if necessary
  - Any bugs found would be fixed in a feature branch, pushed to DEV and then promoted back to QA
  - Helps to act as a shield for our main branch and block any problematic code even further from reaching PROD
- The final being PROD (main)
  - This is where our fully approved code goes
  - Nothing should exist here that isn't ready to be shown to project partner, TA or Instructors

### Example development steps
1. Create a feature branch from the most up to date code
  - This will be from QA or main. If code has recently been moved from QA to main then main, if not QA

  #### Steps
    a. Go to the repo '<> code' tab
    b. switch to 'main' or 'qa'
    c. click branch dropdown (near the top-left, next to repo name)
    d. Type the name of your new branch (e.g., 'feature/your-feature-name') and press 'Enter'
      - Follow a naming convention that clearly conveys what you're working on
      - Feature branches shouldn't have too many work items to avoid huge code reviews
      
2. Work on your feature, committing regularly and pushing to your feature branch
  - If you haven't already, clone the repo
    - Do this through 'git clone [Repo URL]' in terminal or command prompt
    - Then Navigate to it using 'cd [Your repo name]
  - Switch to your feature branch
    - In the terminal, run 'git checkout feature/your-feature-name'
    - Yay! Now code in your favorite IDE
    - If possible, test and read through your code
   
3. Committing and Pushing Your Changes
  - In your terminal wihtin the project directory
    - Add changes 'git add .'
    - Commit changes 'git commit -m "Describe your changes"'
    - Push changes: 'git push origin feature/your-feature-name'

4. Creatingt a Pull Request
   - Return to GitHub repository in web browser
   - You'll probably see a message about your recently pushed branch
     - Click 'Compare & pull request'
   - Ensure that the "base branch" is 'dev' and the "compare branch" is your feature branch
   - Fill out the pull request details and submit
     
5. Review and Merging
  - Teammates review your PR and leave comments, approve, or request changes
  - Once approved, someone (probably you) clicks 'Merge Pull Request'
    
6. Promote to 'QA'
  - Once 'dev' is ready for testing, you would follow a similar process to merge 'dev' into 'qa'
  - Go to GitHub, create a new pull request
  - Set the "base branch" to 'qa' and "compare branch" to 'dev'
  - Review and merge
    
7. QA Testing and Promotion to 'main' (PROD)
  - Testing done on the 'qa' branch
  - Once testing is complete and everything is approved, create another PR
  - Set "base branch" to 'main' (PROD) and the "compare branch" to 'qa'
  - Review and merge
    
8. Hotfixes to 'main' (PROD)
#### If an urgent fix is needed for PROD:
  a. Create a branch from 'main' (e.g., 'hotfix/urgent-but-fix')
  b. Fix the issue, test locally, commit, and push
  c. Create a pull request from your hotfix branch to 'main'
  d. After merging to 'main', ensure to also merge the changes back to 'dev' and 'qa'

### Notes
  - Always pull the latest changes from the branch you are branching off from to avoid conflicts
    - use 'git pull origin branch_name'
  - Make sure to regularly communicate with the team to avoid overlapping work and merge conflicts


## Environment Configuration

  - Use '.env' files or similar in your codebase
  - **Do not commit secrets** like API keys to the repo. Instead, use GitHub Secrets
    a. In GitHub, go to the repo > "Settings" > "Secrets"
    b. Add secrets like 'DATABASE_URL', 'API_KEY', etc
    c. In our GitHub Actions workflow, we can use these secrets with '${{secrets.SECRET_NAME}}'

## Database Migrations

  - Use a Python-based migration tool such as Flask-Migrate, which is an extension that integrates Alembic with Flask applications. This tool is suitable for handling SQLAlchemy database migrations.

  - Within our CI/CD pipeline (GitHub Actions), it's essential to apply database migrations to ensure the database schema is up-to-date with our codebase:

    1. After the test step and before deployment in the GitHub Actions workflow, include a step to run database migrations.
    2. Use the command flask db upgrade to apply the migrations to your database.
    3. Ensure the workflow has the necessary environment variables and database access to perform the migrations successfully.

## Access Control

  - Only teammembers and project parter should be able to merge into 'qa' and 'main'
