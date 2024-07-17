# Log Parsing Project

Welcome to the "Log Parsing" project! In this project, you will apply your knowledge of Python programming to parse and process data streams in real-time. The main tasks involve reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data. Below are the key concepts and resources that will guide you through this project.

## Concepts Needed

### File I/O in Python
- **Understand how to read from sys.stdin line by line**:
  - This is crucial for processing data as it streams in.
  - Resource: [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

### Signal Handling in Python
- **Handling keyboard interruption (CTRL + C) using signal handling in Python**:
  - Learn to gracefully handle interruptions to ensure your program exits cleanly.
  - Resource: [Python Signal Handling](https://docs.python.org/3/library/signal.html)

### Data Processing
- **Parsing strings to extract specific data points**:
  - You'll need to break down each line of input to extract relevant information.
- **Aggregating data to compute summaries**:
  - Once data points are extracted, you'll need to aggregate them for summary statistics.

### Regular Expressions
- **Using regular expressions to validate the format of each line**:
  - Regular expressions are a powerful tool for ensuring that each log entry matches the expected format.
  - Resource: [Python Regular Expressions](https://docs.python.org/3/library/re.html)

### Dictionaries in Python
- **Using dictionaries to count occurrences of status codes and accumulate file sizes**:
  - Dictionaries are ideal for counting occurrences and accumulating data in an efficient manner.
  - Resource: [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### Exception Handling
- **Handling possible exceptions that may arise during file reading and data processing**:
  - Robust exception handling ensures that your program can deal with unexpected issues gracefully.
  - Resource: [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
