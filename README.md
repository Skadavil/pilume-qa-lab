# PiLume QA Lab

**Work in progress:** a Raspberry Pi test bench for validating connected RGB-lighting hardware and its control application.

PiLume is a portfolio project focused on technical product testing, not only device control. It demonstrates hardware-software integration, test design, boundary validation, fault reproduction, event logging, regression testing, and clear technical documentation.

The project currently runs in **simulation mode**. Physical RGB LED and sensor integration is the next milestone.

## Project goals

- Control an RGB light through a REST API
- Validate brightness and colour inputs at normal, boundary, and invalid values
- Record timestamped device events for troubleshooting and test evidence
- Build repeatable automated API and hardware tests
- Reproduce faults and document defects, fixes, and regression results
- Provide a phone-friendly interface for manual exploratory testing

## Current status

### Implemented

- FastAPI application running on Raspberry Pi
- Simulated RGB-light state and on/off control
- Brightness validation from 0 to 100
- Red, green, and blue validation from 0 to 255
- Timestamped in-memory event history
- Interactive API documentation through Swagger UI
- Automated tests with `pytest`

### Verified test result

Six automated tests currently pass, covering API availability, state changes, validation, switch-off behaviour, and event creation.

## Architecture

```text
Phone or computer
        |
        | HTTP / REST
        v
FastAPI application
        |
        +---- simulated light state
        |
        +---- timestamped event log
        |
        +---- automated pytest checks
        |
        `---- GPIO hardware layer (planned)
```

## Repository structure

```text
pilume-qa-lab/
|-- src/
|   `-- pilume/
|       |-- __init__.py
|       |-- main.py
|       `-- event_log.py
|-- tests/
|   `-- test_api.py
|-- README.md
`-- .gitignore
```

## Requirements

- Raspberry Pi with Raspberry Pi OS
- Python 3.13.5 (the current development version)
- Git
- Internet access during dependency installation


## Installation

Clone the repository and enter the project folder:

```bash
git clone git@github.com:Skadavil/pilume-qa-lab.git
cd pilume-qa-lab
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the current dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install fastapi "uvicorn[standard]" pytest httpx
```

## Run the application

From the repository root, with the virtual environment active:

```bash
PYTHONPATH=src uvicorn pilume.main:app --host 0.0.0.0 --port 8000
```

Open the following addresses on the Raspberry Pi or another device connected to the same network:

- Application status: `http://<raspberry-pi-ip>:8000/`
- Interactive API documentation: `http://<raspberry-pi-ip>:8000/docs`
- Current light status: `http://<raspberry-pi-ip>:8000/api/status`
- Event history: `http://<raspberry-pi-ip>:8000/api/events`

## API endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/` | Confirm that PiLume is running |
| `GET` | `/api/status` | Read the current simulated light state |
| `POST` | `/api/light` | Set brightness and RGB values |
| `POST` | `/api/light/off` | Switch the light off |
| `GET` | `/api/events` | Read the timestamped event history |

Example light command:

```json
{
  "brightness": 75,
  "red": 20,
  "green": 40,
  "blue": 60
}
```

## Run the tests

```bash
PYTHONPATH=src pytest -v
```

The tests are designed to verify both expected behaviour and invalid inputs. This provides a regression baseline before physical hardware is introduced.

## Test approach

The project will combine several forms of product testing:

- **Functional testing:** confirm that controls produce the expected state
- **Boundary testing:** check minimum and maximum brightness and RGB values
- **Negative testing:** reject malformed or out-of-range requests
- **Integration testing:** verify communication between the API and GPIO hardware
- **Exploratory testing:** test real usage from a phone or computer
- **Fault testing:** simulate connection loss, sensor errors, and hardware failures
- **Regression testing:** rerun automated checks after every change

## Hardware plan

The next stage will use components from a Raspberry Pi electronics starter kit:

- Breadboard RGB LED with current-limiting resistors
- Push button for physical input testing
- Photoresistor for light-response tests
- Thermistor for temperature monitoring
- Jumper wires and breadboard

The software will keep a simulation mode so automated tests can run without hardware attached.

## Safety

Raspberry Pi GPIO uses 3.3 V logic. LEDs must use suitable current-limiting resistors. Do not connect a 5 V signal directly to a GPIO pin, and do not power high-current lighting directly from GPIO.

## Roadmap

- [x] Build the simulation-mode REST API
- [x] Add input validation and automated API tests
- [x] Add timestamped event logging
- [ ] Connect and control a breadboard RGB LED
- [ ] Add button and light-sensor input
- [ ] Add a phone-friendly control page
- [ ] Generate HTML test reports
- [ ] Create fault-injection scenarios
- [ ] Document a sample defect, fix, and regression result
- [ ] Add wiring diagrams, photographs, and a demonstration video

## Portfolio context

PiLume was started as a practical portfolio project for a transition from software development into technical product testing. It combines a long-standing interest in electronics with professional development experience and a strong interest in software quality and hands-on testing.

## Author

Developed by **Shehfinaz Kadavil** as an independent Raspberry Pi hardware-and-app testing project.
