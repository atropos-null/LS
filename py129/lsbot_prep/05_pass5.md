# PY129 LSBOT Prep Questions

## Pass 5, Exceptions

### 58. Advanced: Custom Exception Hierarchy for Data Validation

Create a custom exception hierarchy for a data processing application.
1. Define a base exception class called `DataValidationError`.
2. Define two specific exception classes that inherit from `DataValidationError`: `MissingDataError` and `InvalidTypeError`.
3. Write a function `validate_user_data(data)` that takes a dictionary. 
    * It should raise `MissingDataError` if the required keys `'username'` or `'email'` are missing. 
    * It should raise `InvalidTypeError` if `'username'` or `'email'` are not strings.
4. If the data is valid, the function should return `True`.

Test cases:

```python

try:
    print(validate_user_data({'username': 'testuser', 'email': 'test@example.com'}))
except DataValidationError as e:
    print(e)
# Expected: True

# Missing 'email'
try:
    validate_user_data({'username': 'testuser'})
except DataValidationError as e:
    print(f"Caught expected error: {type(e).__name__} - {e}")
# Expected: Caught expected error: MissingDataError - Missing required key: 'email'

# Invalid type for 'username'
try:
    validate_user_data({'username': 123, 'email': 'test@example.com'})
except DataValidationError as e:
    print(f"Caught expected error: {type(e).__name__} - {e}")
# Expected: Caught expected error: InvalidTypeError - 'username' must be a string.
```

<details> 
<summary>Possible Solution</summary> 

```python
class DataValidationError(Exception):
    
    def __init__(self, message):
        super().__init__(message)

class MissingDataError(DataValidationError):
    pass

class InvalidTypeError(DataValidationError):
    pass


def validate_user_data(data):
    def validate_user_data(data):
    required_keys = ['username', 'email']
    
    # Check for missing keys
    for key in required_keys:
        if key not in data:
            raise MissingDataError(f"Missing required key: '{key}'")
    
    # Check for invalid types
    for key in required_keys:
        if not isinstance(data[key], str):
            raise InvalidTypeError(f"'{key}' must be a string.")
            
    return True


try:
    print(validate_user_data({'username': 'testuser', 'email': 'test@example.com'}))
except DataValidationError as e:
    print(e)
# Expected: True

# Missing 'email'
try:
    validate_user_data({'username': 'testuser'})
except DataValidationError as e:
    print(f"Caught expected error: {type(e).__name__} - {e}")
# Expected: Caught expected error: MissingDataError - Missing required key: 'email'

# Invalid type for 'username'
try:
    validate_user_data({'username': 123, 'email': 'test@example.com'})
except DataValidationError as e:
    print(f"Caught expected error: {type(e).__name__} - {e}")
# Expected: Caught expected error: InvalidTypeError - 'username' must be a string.
```

</details>

### 59. Advanced: Resource Cleanup with `finally`

Simulate a resource connection (like a database or network socket) that must always be closed.vCreate a class `ResourceConnector` with `connect`, `process_data`, and `disconnect` methods. The `process_data` method should simulate a potential error. Write a function `process_resource(connector)` that ensures `disconnect` is always called, whether `process_data` succeeds or fails with an exception.

Test Cases:

```python
class ResourceConnector:
    def __init__(self, name):
        self.name = name
        self.connected = False

    def connect(self):
        print(f"Connecting to {self.name}...")
        self.connected = True

    def disconnect(self):
        print(f"Disconnecting from {self.name}...")
        self.connected = False

    def process_data(self, fail=False):
        if not self.connected:
            raise ConnectionError("Not connected.")
        if fail:
            print("Processing failed!")
            raise ValueError("Simulated processing error")
        print("Processing data successfully.")

def process_resource(connector, should_fail=False):
    # Your implementation here
    pass

# Successful run
res1 = ResourceConnector("DB1")
process_resource(res1, should_fail=False)

print("-" * 20)

# Failing run
res2 = ResourceConnector("API2")
process_resource(res2, should_fail=True)
```
Expected Output:

```
Connecting to DB1...
Processing data successfully.
Disconnecting from DB1...
--------------------
Connecting to API2...
Processing failed!
Disconnecting from API2...
Caught a processing error: Simulated processing error
```

<details> 
<summary>Possible Solution</summary> 

```python
class ResourceConnector:
    def __init__(self, name):
        self.name = name
        self.connected = False

    def connect(self):
        print(f"Connecting to {self.name}...")
        self.connected = True

    def disconnect(self):
        print(f"Disconnecting from {self.name}...")
        self.connected = False

    def process_data(self, fail=False):
        if not self.connected:
            raise ConnectionError("Not connected.")
        if fail:
            print("Processing failed!")
            raise ValueError("Simulated processing error")
        print("Processing data successfully.")

def process_resource(connector, should_fail=False):
    connector.connect()
    try:
        connector.process_data(fail=should_fail)
    finally:
        # This block ALWAYS runs, even if an exception occurs above
        connector.disconnect()

# Successful run
res1 = ResourceConnector("DB1")
process_resource(res1, should_fail=False)

print("-" * 20)

# Failing run
res2 = ResourceConnector("API2")
process_resource(res2, should_fail=True)
```

</details>

### 60. Advanced: Exception Chaining

Write a function `load_config(config_dict)` that processes a configuration dictionary. If a required key `'db_host'` is missing, it should catch the `KeyError` and raise a new `ConfigurationError` that includes the original exception as its cause. This is known as exception chaining.

Test Cases:
```python
class ConfigurationError(Exception):
    """Error in application configuration."""
    pass

def load_config(config_dict):
    # Your implementation here
    pass

# Successful case
try:
    host = load_config({'db_host': 'localhost'})
    print(f"DB Host: {host}")
except ConfigurationError as e:
    print(e)

# Failing case
try:
    load_config({'user': 'admin'})
except ConfigurationError as e:
    print(f"Configuration Error: {e}")
    print(f"Original cause: {e.__cause__}")
```

Expected Output:
```
DB Host: localhost
Configuration Error: Missing required configuration key: 'db_host'
Original cause: 'db_host'
```

<details> 
<summary>Possible Solution</summary> 

```python

class ConfigurationError(Exception):
    def __init__(self, message):
        super().__init__(message)


def load_config(config_dict):

    try:
        return config_dict['db_host']
    except KeyError as e:

        raise ConfigurationError(f"Config failed: '{e.args[0]}' is missing") from e


# Successful case
try:
    host = load_config({'db_host': 'localhost'})
    print(f"DB Host: {host}")
except ConfigurationError as e:
    print(e)

# Failing case
try:
    load_config({'user': 'admin'})
except ConfigurationError as e:
    print(f"Configuration Error: {e}")
    print(f"Original cause: {e.__cause__}")
```

</details>


### 61 Advanced: Advanced Setters with Multiple Exception Types

Create a `User` class with a `_email` attribute and a public email property. The setter for the email property must perform the following validations and raise the specified exceptions:

1. `Raise TypeError` if the value is not a string.
2. `Raise ValueError` if the string does not contain an @ symbol.
3. `Raise ValueError` if the string is less than 5 characters long.

Test Cases:

```python
class User:
    # Your implementation here
    pass

def create_user(email):
    try:
        user = User(email)
        print(f"User created with email: {user.email}")
    except (TypeError, ValueError) as e:
        print(f"Error: {type(e).__name__} - {e}")

create_user("test@example.com")
create_user(12345)
create_user("test.com")
create_user("a@b")
```

Expected Output:

```
User created with email: test@example.com
Error: TypeError - Email must be a string.
Error: ValueError - Email must contain an '@' symbol.
Error: ValueError - Email must be at least 5 characters long.
```

<details> 
<summary>Possible Solution</summary> 

```python
class User:
    
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string")
        if "@" not in value:
            raise ValueError("Must have an @ symbol")
        if len(value) < 5:
            raise ValueError("Must be 5 characters or more")
        self._email = value
        
def create_user(email):
    try:
        user = User(email)
        print(f"User created with email: {user.email}")
    except (TypeError, ValueError) as e:
        print(f"Error: {type(e).__name__} - {e}")

create_user("test@example.com")
create_user(12345)
create_user("test.com")
create_user("a@b")
```

</details>


### 62. Advanced: Refactoring a Poor Exception Handler

The following function uses a broad except clause that hides bugs and makes debugging difficult. Refactor `process_data` to handle `ValueError` and `IndexError` specifically with different messages, and let any other unexpected exceptions propagate.

Original Code:
```python
def process_data(data_list, index):
    try:
        value = int(data_list[index])
        result = 100 / value
        print(f"Result is {result}")
    except: # This is too broad
        print("An unspecified error occurred.")
```

**Refactored Function Signature**: `def process_data_refactored(data_list, index):`

Test Cases:

```python
# Should print "Invalid data format: cannot convert to integer."
process_data_refactored(['10', '20', 'abc'], 2)

# Should print "Invalid index: index is out of range."
process_data_refactored(['10', '20', '30'], 5)

# Should raise a ZeroDivisionError
try:
    process_data_refactored(['10', '0', '30'], 1)
except ZeroDivisionError as e:
    print(f"Caught an unexpected but specific error: {e}")
```

<details> 
<summary>Possible Solution</summary> 

```python
def process_data_refactored(data_list, index):

    try:
        value = int(data_list[index])
        result = 100 / value
        print(f"Result is {result}")
    except ValueError as e:
        print("Invalid data format: cannot convert to integer.")
    except IndexError as e:
        print("Invalid index: index is out of range")


# Should print "Invalid data format: cannot convert to integer."
process_data_refactored(['10', '20', 'abc'], 2)

# Should print "Invalid index: index is out of range."
process_data_refactored(['10', '20', '30'], 5)

# Should raise a ZeroDivisionError
try:
    process_data_refactored(['10', '0', '30'], 1)
except ZeroDivisionError as e:
    print(f"Caught an unexpected but specific error: {e}")
```

</details>

### 63. Advanced: Meaningful Use of the else Block

Write a function `attempt_connection()` that simulates trying to connect to a service. The connection attempt might raise a `TimeoutError`. If the connection is successful (no exception), the function should print `"Connection successful."` and then `"Processing data..."`. The `"Processing data..."` message must be in an `else` block to ensure it only runs on a successful connection attempt. A "Cleanup" message should always be printed.

Test Cases:

```python
def attempt_connection(should_fail=False):
    print("Attempting to connect...")
    try:
        if should_fail:
            raise TimeoutError("Connection timed out")
        # Simulate successful connection
    except TimeoutError as e:
        print(f"Error: {e}")
    # Your else/finally blocks here

attempt_connection(should_fail=False)
print("-" * 20)
attempt_connection(should_fail=True)
```

Expected Output:

```
Attempting to connect...
Connection successful.
Processing data...
Cleanup.
--------------------
Attempting to connect...
Error: Connection timed out
Cleanup.
```

<details> 
<summary>Possible Solution</summary> 

```python
def attempt_connection(should_fail=False):
    print("Attempting to connect...")
    try:
        if should_fail:
            raise TimeoutError("Connection timed out")
        # Simulate successful connection
    except TimeoutError as e:
        print(f"Error: {e}")
    else:
        print("Connection successful.")
        print("Processing data...")
    finally:
        print("Cleanup.")

attempt_connection(should_fail=False)
print("-" * 20)
attempt_connection(should_fail=True)
```

</details>

### 64. Advanced: Custom Exception with Additional Context

Create a custom exception `TransactionError` that, in addition to a message, stores the `transaction_id` and an `error_code`.  Write a function `process_transaction(tx_id, amount)` that raises this exception with relevant context if the amount is negative.

Test Cases:

```python
class TransactionError(Exception):
    # Your implementation here
    pass

def process_transaction(tx_id, amount):
    print(f"Processing transaction {tx_id}...")
    if amount < 0:
        raise TransactionError(
            "Transaction amount cannot be negative.",
            transaction_id=tx_id,
            error_code=101
        )
    print("Transaction successful.")

try:
    process_transaction("TX123", 100)
    process_transaction("TX456", -50)
except TransactionError as e:
    print(f"\nTransaction failed!")
    print(f"  Message: {e}")
    print(f"  Transaction ID: {e.transaction_id}")
    print(f"  Error Code: {e.error_code}")
```

Expected Output:

```
Processing transaction TX123...
Transaction successful.
Processing transaction TX456...

Transaction failed!
  Message: Transaction amount cannot be negative.
  Transaction ID: TX456
  Error Code: 101
```

<details> 
<summary>Possible Solution</summary> 

```python
class TransactionError(Exception):

    def __init__(self, message, transaction_id, error_code):
        super().__init__(message)
        self.transaction_id = transaction_id
        self.error_code = error_code
    

def process_transaction(tx_id, amount):
    print(f"Processing transaction {tx_id}...")
    if amount < 0:
        raise TransactionError(
            "Transaction amount cannot be negative.",
            transaction_id=tx_id,
            error_code=101
        )
    print("Transaction successful.")

try:
    process_transaction("TX123", 100)
    process_transaction("TX456", -50)
except TransactionError as e:
    print(f"\nTransaction failed!")
    print(f"  Message: {e}")
    print(f"  Transaction ID: {e.transaction_id}")
    print(f"  Error Code: {e.error_code}")
```

</details>

### 65. Advanced: Selective Exception Handling and Re-raising


Write a function that processes a list of division operations. It should handle `ZeroDivisionError` by logging a warning but continuing. It should handle `TypeError` by stopping immediately but providing a specific error message. Any other exception should be caught and re-raised as a `RuntimeError`.

**Function Signature**: `def process_divisions(operations)`: where operations is a list of tuples (numerator, denominator).

Test Cases:

```python
def process_divisions(operations):    # Your implementation here    
    pass

ops1 = [(10, 2), (20, 5), (30, 0), (40, 8)]
print("--- Processing ops1 ---")
process_divisions(ops1)

ops2 = [(10, 2), (20, 'a'), (30, 5)]
print("\n--- Processing ops2 ---")
process_divisions(ops2)

ops3 = [(10, 2), (None, 5)]
print("\n--- Processing ops3 ---")
try:    
    process_divisions(ops3)
except RuntimeError as e:    
    print(f"Caught re-raised error: {e}")    
    print(f"Original cause: {e.__cause__}")
```

Expected Output:

```
--- Processing ops1 ---
Result: 5.0
Result: 4.0
Warning: Cannot divide by zero. Skipping operation (30, 0).
Result: 5.0
--- Processing ops2 ---
Result: 5.0
Error: Invalid type for division: unsupported operand type(s) for /: 'int' and 'str'
--- Processing ops3 ---
Result: 5.0
Caught re-raised error: An unexpected error occurred during division.
Original cause: unsupported operand type(s) for /: 'NoneType' and 'int'
```

<details> 
<summary>Possible Solution</summary> 

```python
def process_divisions(operations):
    for num, den in operations:
        try:
            result = num / den
            print(f"{num} / {den} = {result}")
            
        except ZeroDivisionError:
            print(f"Warning: Cannot divide {num} by zero. Skipping.")
            continue  # Moves to the next item in the list
            
        except TypeError as e:
            if isinstance(num, str) or isinstance(den, str):
                print(f"Stopping: Invalid input types (found a string: '{num}' or '{den}').")
                return # Stops the function immediately
            
            # If it's a TypeError but not a string (like 'None'), 
            # we treat it as an "any other exception" case.
            raise RuntimeError("A type-related processing error occurred.") from e
            
        except Exception as e:
            # 3. Any other exception: catch and re-raise as RuntimeError
            raise RuntimeError("An unexpected error occurred during processing.") from e

# --- Test Cases ---

ops1 = [(10, 2), (20, 5), (30, 0), (40, 8)]
print("--- Processing ops1 ---")
process_divisions(ops1)
# Result: Processes everything, skips (30, 0) with a warning.

ops2 = [(10, 2), (20, 'a'), (30, 5)]
print("\n--- Processing ops2 ---")
process_divisions(ops2)
# Result: Processes (10, 2), then stops immediately on 'a'.

ops3 = [(10, 2), (None, 5)]
print("\n--- Processing ops3 ---")
try: 
    process_divisions(ops3)
except RuntimeError as e: 
    print(f"Caught re-raised error: {e}") 
    print(f"Original cause: {repr(e.__cause__)}")
# Result: Processes (10, 2), then re-raises the None error as a RuntimeError.
```
</details>

