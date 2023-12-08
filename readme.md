# Homework 5

**We will be taking 2 more of our 5 late days (we previously took 2). This assignment will be submitted by Friday 10:00 am**

This repository some of the answers to homework. Answers which have been done in other repositories have been linked below.  This project is done by Nishant Aggarwal ([@n-aggarwal](https://github.com/n-aggarwal)) and Anan Afrida ([@ananafrida](https://github.com/ananafrida)). We distributed the work as follows after discussion: <br />
<br />
Nishant: 2,3,6 <br />
Anan: 1,4,5

Problem 1,2, and 6 can be found in this repository. <br />
Problem 3 can be found in the [backend repo for homework 3](https://github.com/n-aggarwal/comp-333-3-backend). Instructions for setting up the enviornment for question 3 are given at the bottom of the readme of the linked repo.

## Unit Test (Problem 1) - Anan
This problem's code can be found under unit_testing.py file. Run the file as a regular python file using "python unit_testing.py"

## Pytest (Problem 2) - Nishant

This section of the readme provides instructions on how to run the "pytest" tests.

### Setting up the environment

I will assume that you already have python installed on your machine. If not, you can downlaod it using homebrew or through the [python website](https://www.python.org/).

Next, you need to install pytest on your machine. To install pytest run the following command:

```bash
pip3 install pytest
```



or if you have on older version of python:

```bash
pip install pytest
```

### Running the tests

Now to run the tests, in your terminal change to the directory `problem_2`. Now just run the following command:

```bash
$ v stands for verbose
pytest -v
```

You should see the desired output.


## Frontend jestJS testing (Problem 4) - Anan
** For problem 4 and problem 5, please refer to this GitHub repo [frontend repo for homework 3](https://github.com/ananafrida/comp-333-3-frontend) **
This section provides frontend setup using jestJS for frontend testing:

### Part 1: Setup
Create your frontend unit tests using [Jest](https://jestjs.io/), a unit
testing framework for Javascript and React.

1. Unit testing with Jest will require you to include files in different places
   of your existing React app frontend. Thus, it is a good idea to make a local
   copy of your app to experiment with it.
2. Jest comes included with React, however, you can install it in the root folder
   of your copied repo to make sure:

   ```bash
   npm install --save-dev jest @testing-library/react @testing-library/jest-dom
   ```

3. Navigate to the root folder of your frontend, where you keep your
   `package.json`.
4. Place your unit test files in the designated folders they relate to. For example,
   your login unit tests would go into the folder of your login view. If your
   login view is named `login.js`, your related test file would be named
   `login.test.js`.
5. Run your tests from within your frontend root folder with:

   ```bash
   npm test a
   ```
   **Make sure to use the filter a to run all our test files.**

### Part 2: Login/Registration Unit Testing:
1. For a, c, d: Place your unit test under root_directory --> src --> components --> login_component.test.js for login.
2. For a, c, d: Place your unit test under the root_directory --> src --> components --> register_component.test.js for register
3. Since we didn't have a navigation link under login or registration, we covered (b) under the homeView (please refer to the next point).
4. For b: Place your unit tests under root_directory --> src --> views --> homeView.test.js for navigation link testing


## GitHub CI (Problem 5) - Anan
You can find our yaml file under the github actions tab.

## Generative AI Tool (Problem 6) - Nishant
I personally did not use any AI tools to assist me with testing, except for general
debugging of the code, but I can see where it can be used. I don't think that 
generative AI tools would be too helpful for unit testing because there is a chance that
it incorrectly guesses the "actual value" when writing tests, which could cause a lot of
problems. Instead, I think generative AI may be more helpful in end-to-end testing, 
acting in a way similar to a real user. It could help spot problems in perhaps the UI, 
or the design of the program, and help give the developers a feel of how real users might
use their platform. By using generative AI, rather than actual users or pre written 
scripts in Selenium for end-to-end testing, developers could potentially save a lot of 
money, and  reduce time spent on testing.

As an example: I gave chatGPT my unit-tests code (AllTests.php) and asked it to write an 
end-to-end test simulating how a user may call various API's, and s stress test for my 
application. The results are given below:

End-to-End testing:

    public function testCompleteUserScenario(): void
    {
        // Register a new user
        $registrationResponse = $this->registerUser('test_user', '1234567890', '1234567890');
        $this->assertTrue($registrationResponse['success']);

        // Login with the registered user
        $loginResponse = $this->loginUser('test_user', '1234567890');
        $this->assertTrue($loginResponse['success']);

        // Add a new song
        $addSongResponse = $this->addNewSong('test_artist', 'test_song', '4');
        $this->assertTrue($addSongResponse['success']);

        // Get the list of songs
        $songListResponse = $this->getSongList();
        $this->assertEquals(200, $songListResponse['statusCode']);
        $this->assertIsArray($songListResponse['data']);

        // Update a song
        // Note: Ensure 'id' corresponds to an existing song ID
        $updateSongResponse = $this->updateSong(55, 'update_artist', 'update_song', '3');
        $this->assertTrue($updateSongResponse['success']);

        // Delete a song
        // Note: Ensure 'id' corresponds to an existing song ID
        $deleteSongResponse = $this->deleteSong(56);
        $this->assertTrue($deleteSongResponse['success']);
    }

Stress-Testing:

    public function testStressServerWithMultipleRequests(): void
    {
        $concurrentRequests = 50; // Number of concurrent requests to simulate
        $totalRequests = 200; // Total number of requests to send

        $responses = [];
        $exceptionCount = 0;

        // Initiate multiple asynchronous requests
        $promises = [];
        for ($i = 0; $i < $concurrentRequests; $i++) {
            $promises[] = $this->client->getAsync('index.php'); // Change the endpoint accordingly
        }

        // Execute the requests asynchronously
        try {
            $responses = GuzzleHttp\Promise\settle($promises)->wait();
        } catch (GuzzleHttp\Exception\RequestException $e) {
            $exceptionCount++;
        }

        // Evaluate the responses and exceptions
        $successfulResponses = 0;
        foreach ($responses as $response) {
            if ($response['state'] === 'fulfilled' && $response['value']->getStatusCode() === 200) {
                $successfulResponses++;
            }
        }

        // Check if the number of successful responses meets expectations
        $this->assertGreaterThanOrEqual(
            $totalRequests - $exceptionCount,
            $successfulResponses,
            "Failed to receive expected successful responses."
        );
    }

Although these responses are pretty good, there is still a lot of room for improvement.
If you look through the stress test, I still have to manually change the endpoint, 
and it isn't testing multiple endpoints at the same time. Also with the end-to-end
testing, it is very rigid taking values from my previous test, and not adapting. This
could probably be improved by the use of specialized AI technologies designed for testing.

I also trieds using an extenstion in VScode called "Software Testing AI" through which
highlighting a function should prodcue tests for it but unfortunaltely it did not 
support php at the moment. 

*** I mistakenly pushed a snippet of my code to the main branch without noticing which branch I was checked out to. Kindly disregard that commit. ***
