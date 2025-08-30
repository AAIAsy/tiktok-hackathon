# Introduction

This repo is created for a hackathon challenge by TikTok. The process from getting raw review data and metadata to model training and data analysis will be discussed in the following sections.

## Overview

### Problem statement

The following is the problem statement provided by the organizing party, TikTok:

Online reviews play a crucial role in shaping public perception of local businesses and locations. However, the presence of irrelevant, misleading, or low-quality reviews can distort the true reputation of a place. With the proliferation of user-generated content, ensuring the quality and relevancy of reviews is more important than ever. This hackathon challenges students to leverage Machine Learning (ML) and Natural Language Processing (NLP) to automatically assess the quality and relevancy of Google location reviews, aligning them with a set of well-defined policies. The ultimate goal is to improve the reliability of review platforms and enhance user experience.


### Objectives

Tiktok has outlined clear objectives that should be met by the end of the 72-hour hackathon challenge:

- Gauge review quality: Detect spam, advertisements, irrelevant content, and rants from users who have likely never visited the location.
- Assess relevancy: Determine whether the content of a review is genuinely related to the location being reviewed.
- Enforce policies: Automatically flag or filter out reviews that violate the following example policies:
  - No advertisements or promotional content.
  - No irrelevant content (e.g., reviews about unrelated topics).
  - No rants or complaints from users who have not visited the place (can be inferred from content, metadata, or other signals).
