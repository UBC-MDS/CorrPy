# Contributing

In this project, we will be using git as the version control system for our work. By participating in this project, each group member should agree to abide by the [code of conduct](https://github.com/UBC-MDS/DSCI524_lab03_group15/blob/master/CONDUCT.md). Each group member will fork the main repository into their personal repository. They will work locally, and send pull-requests of their update to the main repository. At least one other team mate will review,  critique (if necessary), and finally accept their team mate's pull request. Each contributor will also use GitHub issue to communicate to their team mates regarding any problems, ideas and concerns.

The full instructions can be found from the [Github guides to Forking](https://guides.github.com/activities/forking/).

### Example of a contributing workflow:

Fork, then clone the repo:
```
git clone https://github.com/<your_username>/DSCI524_lab03_group15.git
```

Make changes, then push the repo:
```
git add .
git commit -m "<meaningful_message>"
git push
```

Check if the main repo is added as a remote repo:
```
git remote -v
```

If the main repo is not added:
```
git remote add upstream <original_repo_URL>
```

If the current `master` branch falls behind the forked branch:
```
git fetch upstream
git merge upstream/master
git push
```
Push to your fork and submit a pull request for other team mates to review.

Contributing document derived from [Thoughtbot](https://github.com/thoughtbot/factory_bot_rails/blob/master/CONTRIBUTING.md).
