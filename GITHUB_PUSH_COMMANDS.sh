#!/bin/bash

# SauceDemo Automation - GitHub Push Commands
# Copy and paste these commands in order to push your project to GitHub

echo "================================"
echo "GitHub Push Commands - Copy & Paste"
echo "================================"
echo ""
echo "STEP 1: Create GitHub Repository"
echo "1. Go to https://github.com/new"
echo "2. Repository name: saucedemo-automation"
echo "3. Description: End-to-end automation testing suite for SauceDemo using Selenium and Pytest"
echo "4. Visibility: Public"
echo "5. Click 'Create repository'"
echo ""
echo "STEP 2: Run these commands in your terminal:"
echo ""
echo "========== COPY THESE COMMANDS =========="
echo ""

cat << 'EOF'
# Navigate to project directory
cd /Users/mt/saucedemo-automation

# Add remote repository (replace Seoback04 with your GitHub username if different)
git remote add origin https://github.com/Seoback04/saucedemo-automation.git

# Verify remote was added
git remote -v

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub (you may be prompted for GitHub credentials)
git push -u origin main

# Verify push was successful
git log --oneline -3

EOF

echo ""
echo "========== END OF COMMANDS =========="
echo ""
echo "STEP 3: After pushing, verify on GitHub:"
echo "1. Go to https://github.com/Seoback04/saucedemo-automation"
echo "2. Check that all files are visible"
echo "3. Verify README.md renders properly"
echo ""
echo "STEP 4: Update your GitHub profile:"
echo "1. Go to https://github.com/Seoback04/settings"
echo "2. Update bio: 'QA Automation Engineer | Python | Selenium | Pytest'"
echo "3. Go to profile and click 'Customize your pins'"
echo "4. Select saucedemo-automation and move to top"
echo ""
echo "Done! Your project is now on GitHub 🎉"
