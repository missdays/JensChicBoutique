# Jen's Chic Boutique Web Development Project

Welcome to the Jen's Chic Boutique web development project repository! This project is designed to provide a comprehensive e-commerce platform for managing product items and user accounts.

![alt text](img1.png)

![alt text](img2.png)

![alt text](img3.png)

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Manual Testing](#manual-testing)
- [Deployment](#deployment)
- [User Stories](#user-stories)
- [Future Features](#future-features)
- [Bugs](#bugs)
- [Credits](#credits)

## Introduction
Jen's Chic Boutique is a web development project designed to make managing boutique items and user accounts easy. It features a user-friendly interface for customers. 

## Technologies Used
The project is built using the following technologies:

- Django
- Django AllAuth
- HTML/CSS/JavaScript 
- Git/GitHub (Version Control)
- Heroku (Cloud-based Platform)

## Project Structure
- **Root Directory**: Contains the main Django project files, `README.md`, and additional helper files (HTML, CSS, JS, IMG).
- **requirements.txt**: Python dependencies list.
- **runtime.txt**: The targeted Python runtime.
- **Django Project**:
  - **jenschicboutique**: Contains the Django project settings and configurations.
- **Django Apps**:
  - **bag**: Handles the boutique items and orders.
  - **wishlist**: Manages user accounts and authentication.
- **Static files**:
  - **static**: Holds CSS, JavaScript, and other static files.
- **Templates**:
  - **templates**: Contains HTML template files.
- **404 Page Implemented**



![Project Structure]

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/jen-chic-boutique.git
   cd jen-chic-boutique
   ```
2. Install Django and add the package to the `requirements.txt` file:
   ```bash
   pip3 install 'django<4’
   pip3 freeze --local > requirements.txt
   ```
3. Create a new Django project and app:
   ```bash
   django-admin startproject jenschicboutique .
   python3 manage.py startapp bag
   python3 manage.py startapp wishlist 
   ```
4. Add the apps to the `INSTALLED_APPS` in `settings.py`.
5. After adding models, run migrations:
   ```bash
   python3 manage.py migrate
   ```
6. Run the development server:
   ```bash
   python3 manage.py runserver
   ```

These steps should prepare your environment. 

## Usage
On the website, users can perform the following actions:

- **Browse Items**: Users can browse product items, search items, choose item’s size, manage bag by adding and removing, 
- **Wishlist**: Users can add items to their wishlist. 
- **Review**: Users can leave a review. 
- **Order Management**: Users can add items to their bag and manage their shopping bag.

![alt text](wish.png)

## Manual Testing
I have tested this website myself to make sure everything works well and it's easy to use by doing the following:

- **Clicked around different pages and features a few times to make sure everything works smoothly.**
- **Tried signing up, logging in, and logging out to see if it all works like it should.**
- **Made sure I could browse items and manage my bag.**
- **Looked at the website on both my computer and phone to make sure it looks good and works right on both.**
- **Checked code for any major bugs.**
- **Tested out all the important features to make sure it all flows smoothly for users.**
- **Kept track of any bugs or issues I ran into while testing and made sure to fix them up.**

## Deployment to Heroku
To deploy your project to Heroku, follow these steps:

1. **Create an account and verify it**:
   - Sign up for a Heroku account and verify your email address.
2. **Create a new app**:
   - Navigate to your Heroku dashboard and create a new app with a unique name.
3. **Update your code for deployment**:
   - Install `gunicorn` and add it to `requirements.txt`:
     ```bash
     pip3 install gunicorn~=20.1
     pip3 freeze --local > requirements.txt
     ```
4. **Enable GitHub integration**:
   - In your app's dashboard, go to the Deploy tab.
   - In the Deployment method section, enable GitHub integration by clicking on "Connect to GitHub".
5. **Select your repository**:
   - Start typing your project repository name into the search box and click Search.
   - Click on the GitHub repository you want to deploy from.
6. **Initiate deployment**:
   - Scroll to the bottom of the page and click "Deploy Branch" to start a manual deployment of the main branch.
7. **View your deployed project**:
   - Once the deployment process is complete, click on "Open app" to view your deployed project.

![Deploy to Heroku]

## User Stories
### User
- I can browse available items.
- I can filter items by name/desc/asc/ price range.
- I can add items to my bag.
- I can remove items from my bag.
- I can update items in my bag. 
- I can see the price updating simultaneously when I edit items in the bag.
- I can add items to wishlist 
- I can leave a review of an item 

![alt text](review1.png)

![alt text](bag.png)

### Administrator
- I can manage product items.
- I can view and manage customer orders.

![alt text](<user story.png>)

## Future Features
- **Order Tracking**: Provide order tracking capabilities.
- **Promotion codes**: Add functionality for promotional codes 
- **Wishlist**: Add a “Add to bag” button to Wishlist. Verify if items are already added to Wishlist.
- **Review** Check if the user has already purchased that item before leaving a review.
- **Registration**: Users can register for an account.
- **Logout**: Users can log out of their accounts.
- Order history 

## Bugs
- Users cannot view their order history.
- Users cannot manage their profile.
- Registration not working for users 
- Logout not working for users 
- CSS and static images not working

### Difficulties Encountered
- Encountered issues with Jquery. Managed to resolve them by following updated documentation. 

## Credits
- Source of  image: Product images by Kaggle.com
- Source of icons: Fontawesome
- Based on the Code Institute Boutique Ado walkthrough 

## Observation 
- To show the css and static images to my project, I would need an Amazon account to connect to AWS swervices, as demonstrated in the walkthrough. However,I wasn't able to proceed with that step. Therefore the project hasn't got any css or images. If the project is ran on Debug mode, css and static images are shown.

The deployment is failing and the cause is unknown. The following log was provided:

```
2024-06-05T11:06:43.001238+00:00 app[web.1]:     self.reap_workers()
2024-06-05T11:06:43.001256+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.12/site-packages/gunicorn/arbiter.py", line 525, in reap_workers
2024-06-05T11:06:43.001345+00:00 app[web.1]:     raise HaltServer(reason, self.WORKER_BOOT_ERROR)
2024-06-05T11:06:43.001374+00:00 app[web.1]: gunicorn.errors.HaltServer: <HaltServer 'Worker failed to boot.' 3>
2024-06-05T11:06:43.080795+00:00 heroku[web.1]: Process exited with status 1
2024-06-05T11:06:43.102343+00:00 heroku[web.1]: State changed from up to crashed
2024-06-05T11:06:44.874199+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=2976e7f8-56f1-42c1-9a32-3da41cd1d91b fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:06:44.950444+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=facc8182-85d4-4a76-89d1-f20b3d0fbe00 fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:06:48.843932+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=3f7e01aa-fdb2-4fd6-8b77-a296d4ad67e1 fwd="194.125.62.26" dyno=web.1 connect=5000ms service= status=503 bytes= protocol=https
2024-06-05T11:06:51.404137+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=e25d429a-cc91-4abc-ac84-7dda512748f7 fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:11:47.243739+00:00 heroku[web.1]: State changed from crashed to starting
2024-06-05T11:11:51.230382+00:00 heroku[web.1]: Starting process with command `gunicorn jenschicboutique:app`
2024-06-05T11:11:51.801039+00:00 app[web.1]: Python buildpack: Detected 512 MB available memory and 8 CPU cores.
2024-06-05T11:11:51.801120+00:00 app[web.1]: Python buildpack: Defaulting WEB_CONCURRENCY to 2 based on the available memory.
2024-06-05T11:11:52.144105+00:00 app[web.1]: [2024-06-05 11:11:52 +0000] [2] [INFO] Starting gunicorn 20.1.0
2024-06-05T11:11:52.144407+00:00 app[web.1]: [2024-06-05 11:11:52 +0000] [2] [INFO] Listening at: http://0.0.0.0:56407 (2)
2024-06-05T11:11:52.144436+00:00 app[web.1]: [2024-06-05 11:11:52 +0000] [2] [INFO] Using worker: sync
2024-06-05T11:11:52.146506+00:00 app[web.1]: [2024-06-05 11:11:52 +0000] [9] [INFO] Booting worker with pid: 9
2024-06-05T11:11:52.148168+00:00 app[web.1]: Failed to find attribute 'app' in 'jenschicboutique'.
2024-06-05T11:11:52.148233+00:00 app[web.1]: [2024-06-05 11:11:52 +0000] [9] [INFO] Worker exiting (pid: 9)
2024-06-05T11:11:52.169825+00:00 app[web.1]: [2024-06-05 11:11:52 +0000] [2] [INFO] Shutting down: Master
2024-06-05T11:11:52.169852+00:00 app[web.1]: [2024-06-05 11:11:52 +0000] [2] [INFO] Reason: App failed to load.
2024-06-05T11:11:52.238870+00:00 heroku[web.1]: Process exited with status 4
2024-06-05T11:11:52.258131+00:00 heroku[web.1]: State changed from starting to crashed
2024-06-05T11:11:54.217590+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=b6694e2f-43ad-41c6-bae0-f688f1b14a45 fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:11:58.228850+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=14572276-9660-4524-9b59-c8efd89a8579 fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:11:59.306048+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=22a606cb-17ed-43f1-a8c8-028dbb797f21 fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:12:04.777786+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=db4bc604-d8df-4e21-a95e-4e1c2109a94c fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:12:04.839393+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=8fecfffd-aef1-49dd-a24a-adfe1268113e fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:11:24.000000+00:00 app[api]: Build started by user dyeneffer13@hotmail.com
2024-06-05T11:12:34.069679+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=da09a4fb-b046-43d5-9cb2-a00cdb68a110 fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:12:34.123067+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=a7fae475-2adf-4155-9a09-47a61a26bbfb fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:12:34.759070+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=6861efc6-1cc7-4744-803a-8cf610823efc fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:12:34.711047+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=8674d095-c13d-43cc-b6b7-5bbc4f916d8d fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:12:34.862301+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=f7bf7584-390e-4f3c-9413-1460f4276b6c fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:12:34.919713+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=54637833-7e2f-412c-a6b6-2626337b41de fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:12:35.138045+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=b6c97010-1b23-44b4-8db8-1ae6e828e385 fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:12:34.988436+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=6a7b7df2-2cf4-4038-9a63-33d3c7c205ff fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:12:35.048384+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=c0f7a66a-63fd-4d71-8e40-97bb0b0917ca fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:12:35.192115+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=jenschicboutique-cc2328e16ed2.herokuapp.com request_id=68250f8d-d108-4107-9b1e-8bfd2cdb5375 fwd="194.125.62.26" dyno= connect= service= status=503 bytes= protocol=https
2024-06-05T11:11:45.916498+00:00 app[api]: Deploy 198afe2e by user dyeneffer13@hotmail.com
2024-06-05T11:11:45.916498+00:00 app[api]: Release v9 created by user dyeneffer13@hotmail.com
2024-06-05T11:11:52.000000+00:00 app[api]: Build succeeded
```