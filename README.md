# Simple Python Calculator with Jenkins - Beginner's Guide

## 🎯 What is This Project?

This is a **very simple** Python calculator that can add two numbers together. It also includes:
- A test to make sure the calculator works correctly
- A Jenkins setup that automatically runs and tests your code

**Perfect for:** Complete beginners who want to learn about automation and testing.

## 📁 What Files Do We Have?

```
simple-calculator/
├── README.md          # This guide you're reading now
├── app.py            # The calculator program (4 math operations)
├── test.py           # Tests to check if the calculator works
├── requirements.txt   # List of Python packages we need
└── Jenkinsfile       # Instructions for Jenkins multibranch pipeline
```

## 🤔 What Does Each File Do?

### app.py - The Calculator
- **4 functions**: add, subtract, multiply, divide
- Asks you to choose which operation you want
- Handles errors (like dividing by zero)
- User-friendly with clear prompts

### test.py - The Tests
- Tests all 4 calculator functions
- Uses **pytest** (a professional testing tool)
- Checks edge cases (like dividing by zero)
- Makes sure your calculator is reliable

### requirements.txt - The Dependencies
- Lists the Python packages we need (like pytest)
- Jenkins will automatically install these
- Keeps track of exact versions for consistency

### Jenkinsfile - The Multibranch Pipeline
- Automatically runs when you push code to any branch
- **Different behavior for different branches:**
  - `dev` → Development environment
  - `staging` → Staging environment
  - `main`/`master` → Production environment

## 🤖 Setting Up Jenkins

### What is Jenkins?
Jenkins is like a helpful robot that:
- Watches your code for changes
- Automatically runs your program
- Automatically runs your tests
- Tells you if something is broken

### Step-by-Step Jenkins Setup

#### Step 1: Install Jenkins
1. Go to [jenkins.io](https://jenkins.io)
2. Download Jenkins for your computer (Windows/Mac/Linux)
3. Follow the installation guide on their website
4. When done, Jenkins will open in your web browser (usually at http://localhost:8080)

#### Step 2: Create Your First Job
1. Click "New Item" in Jenkins
2. Enter a name like "My Calculator"
3. Select "Pipeline" and click OK
4. Scroll down to "Pipeline" section
5. Select "Pipeline script from SCM" if you're using Git, or "Pipeline script" for simple testing

#### Step 3: Connect Your Code
If you're just testing locally:
1. Select "Pipeline script"
2. Copy and paste the contents of your Jenkinsfile into the script box
3. Click "Save"

#### Step 4: Run Your First Build
1. Click "Build Now"
2. Watch Jenkins run your code automatically!
3. If everything works, you'll see a green checkmark ✅
4. If something fails, you'll see a red X ❌

## 📖 Understanding the Results

### When Jenkins Runs Successfully:
- ✅ **Green checkmark**: Everything worked!
- Your calculator ran without errors
- All tests passed
- You're ready to make changes and run again

### When Something Goes Wrong:
- ❌ **Red X**: Something failed
- Click on the build number to see what went wrong
- Common issues:
  - Python not installed
  - File not found
  - Syntax error in your code

## 🛠️ Common Problems and Solutions

### "Python command not found"
**Problem:** Your computer can't find Python
**Solution:** 
- Make sure Python is installed
- Try `python3` instead of `python`
- On Windows, try `py` instead of `python`

### "No module named 'app'"
**Problem:** The test file can't find your main program
**Solution:** 
- Make sure both `app.py` and `test.py` are in the same folder
- Check that you didn't rename the files

## 📚 What You'll Learn

By working with this simple project, you'll understand:

### 🐍 **Python Basics**
- How to write simple functions
- How to test your code
- How to run Python programs

### 🔧 **Testing**
- Why testing is important
- How to write basic tests
- What it means when tests pass or fail

### 🤖 **Automation (CI/CD)**
- How to automatically run your code
- How to catch problems early
- How continuous integration works

## 🎓 Next Steps

Once you're comfortable with this simple calculator:

1. **Add More Functions**: Try adding subtract, multiply, or divide
2. **Add More Tests**: Test edge cases like dividing by zero
3. **Learn Git**: Version control to track your changes
4. **Try Different Branches**: Learn about development vs production
5. **Add Error Handling**: Make your calculator handle invalid inputs

## 🆘 Getting Help

### If You Get Stuck:
1. **Read the error message carefully** - it usually tells you what's wrong
2. **Check that all files are in the same folder**
3. **Make sure Python is installed and working**
4. **Try running each step manually first**

## 🎉 Congratulations!

If you've made it this far and everything is working, you've just:
- ✅ Created your first Python application
- ✅ Written your first test
- ✅ Set up your first automation pipeline
- ✅ Learned the basics of CI/CD

### 🤖 Setting Up Jenkins for Multibranch Pipeline
- First do the Jenkins setup if you haven't already.

1. **In Jenkins, click "New Item"**
2. **Enter name:** "Calculator Multibranch Pipeline"
3. **Select:** "Multibranch Pipeline"
4. **Click "OK"**

5. **Configure Branch Sources:**
   - Click "Add Source" → "Github"
   - **Project Repository:** `(https://github.com/hkm7/calculator-application)`
   - **Credentials:** None 

6. **Configure Build Configuration:**
   - **Mode:** by Jenkinsfile
   - **Script Path:** Jenkinsfile

7. **Save and Scan:**
   - Click "Save"
   - Jenkins will automatically scan and find your branches
   - You should see: `dev`, `staging`, `main` branches detected

## 🔄 How the Multibranch Pipeline Works

### Branch-Specific Behavior:

| Branch | Environment | What Happens |
|--------|-------------|--------------|
| `dev`  | Development | Tests run, deploys to dev environment |
| `staging` | Staging | Tests run, deploys to staging for final testing |
| `main`| Production | Tests run, deploys to production |

### Pipeline Stages:
1. **Setup** - Installs Python packages from requirements.txt
2. **Test** - Runs all tests with pytest
3. **Run App** - Confirms the app is ready
4. **Deploy** - Branch-specific deployment messages

## 🧪 Testing Your Multibranch Pipeline

### Test Development Branch:
```bash
git checkout dev
echo "# Development update" >> README.md
git add .
git commit -m "Test dev branch"
```

### Test Staging Branch:
```bash
git checkout staging
git merge dev  # Get latest changes
git commit -m "Test staging branch"
```

### Test Production Branch:
```bash
git checkout main
git merge staging  # Get tested changes
git commit -m "Test production branch"
```

After each commit, check Jenkins - it should automatically:
- Detect the branch changes
- Run the pipeline for that branch
- Show different deployment messages

## 🛠️ Common WSL/Ubuntu Issues and Solutions

### Python Command Issues:
```bash
# If "python" command doesn't work, use "python3"
# You can create an alias:
echo "alias python=python3" >> ~/.bashrc
echo "alias pip=pip3" >> ~/.bashrc
source ~/.bashrc
```

### Permission Issues:
```bash
# If you get permission errors with pip:
pip3 install --user -r requirements.txt

# Or use virtual environment (recommended):
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📊 What You Should See

### Successful Pipeline Output:
```
Started by branch indexing
Running in Durability level: MAX_SURVIVABILITY
[Pipeline] Start of Pipeline
[Pipeline] stage (Setup)
[Pipeline] { (Setup)
+ python3 --version
Python 3.8.10
+ pip3 install --upgrade pip
+ pip3 install -r requirements.txt
[Pipeline] }
[Pipeline] stage (Test)
[Pipeline] { (Test)
+ python3 -m pytest test.py -v
===== test session starts =====
test.py::test_add PASSED
test.py::test_subtract PASSED
test.py::test_multiply PASSED
test.py::test_divide PASSED
test.py::test_divide_by_zero PASSED
===== 5 passed in 0.02s =====
[Pipeline] }
[Pipeline] stage (Deploy)
🚀 Deploying to PRODUCTION environment
All calculator functions are available in production!
[Pipeline] End of Pipeline
Finished: SUCCESS
```
