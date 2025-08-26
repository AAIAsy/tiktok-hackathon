# Introduction

This repo is created for a hackathon challenge by TikTok.

## Objective

The objective set out by TikTok is outlined as follows:

- Gauge review quality: Detect spam, advertisements, irrelevant content, and rants from users who have likely never visited the location.
- Assess relevancy: Determine whether the content of a review is genuinely related to the location being reviewed.
- Enforce policies: Automatically flag or filter out reviews that violate the following example policies:
  - No advertisements or promotional content.
  - No irrelevant content (e.g., reviews about unrelated topics).
  - No rants or complaints from users who have not visited the place (can be inferred from content, metadata, or other signals).

## Strategy

No fixed strategy is outlined yet. A recommended strategy would be to:
- Define what is a spam, an advertisment, irrelevant contetnt and rant from users who have likely never visited the location
    - This would require knowledge about the place. A description about the place should be looked up as reference.
- Define what kinds of content of a review is related to the location reviewed.
    - Again, this should be about the place. A description of what the place is (whether it is a post office, a restaurant, etc.) is needed for context.

# Setup

## OpenJDK installation
Install the latest Java JDK via Homebrew in order for PySpark to work as we are handling large amounts of data:

```
brew install openjdk@17
```

## Python setup

Create a virtual environment with Python 3.11 and install requirements:

```
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade jupyter
python -m pip install -r requirements.txt
```

## What should be excluded from repo

Dataset should be ignored and prevented from uploading to GitHub due to their large file sizes. Virtual environments must be ignored as well. (Store your dataset in a folder for organization.)

```
touch .gitignore
```

In .gitignore file:

```
# Ignore virtual environments
.venv/

# Ignore dataset
datasets/
```