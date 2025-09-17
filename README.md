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
├── app.py            # The calculator program
├── test.py           # Tests to check if the calculator works
├── requirements.txt  # Install python packages required for the application
└── Jenkinsfile       # Instructions for Jenkins to run everything automatically
```

## 🤔 What Does Each File Do?

### app.py - The Calculator
- This is your main program
- It asks you to enter two numbers
- It adds them together and shows the result
- Very simple - just addition!

### requirements.txt  
- Contains a list of packages required by the application
- Even as new releases are done the same file can be appended with new dependencies
- If you encounter error with installing packages, make sure pip or python3-pip (in ubuntu24+) is installed. Ubuntu 22 or below do not require '--break-system-packages' part to be added

### test.py - The Test
- This file checks if your calculator works correctly
- It tries a few examples (like 2+3=5) to make sure everything is working
- If all tests pass, you know your calculator is working!

### Jenkinsfile - The Automation
- This tells Jenkins (a computer program) how to run your code automatically
- Every time you change your code, Jenkins will run it and test it for you
- No need to remember to run tests manually!

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
