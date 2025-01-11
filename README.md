# Project 1: Collecting data. Linear analysis

Welcome to PHYS/MENG-230! This is the first project, so it makes sense to set up some context. This is a course about two things:

1. Extracting meaning from data **AND**
2. Developing electronics skills to support experimental design.

For each of these larger goals there a number of sub-goals. For example there are three conceptual learning outcomes related to handling data:

1. Generative Models, Estimating Parameters of models (DALO-1)
2. Bayesian Probability and Inference (Bayes Rule, Update, MCMC) (DALO-2)
3. Descriptive Statistics (Mean, variance, standard error,  etc.) (DALO-3)

and there are eight conceptual learning outcomes related to electronics:

1. Ohm’s Law, Voltage Dividers, with resistance and impedance (DC/AC) (ECLO-1)
2. Non-linear, dependent circuit elements (e.g., diodes, transistors) (ECLO-2)
3. Amplifiers and feedback (ECLO-3)
4. Timers, Counters, PWM, etc. (ECLO-4)
5. Communication (RS-232, I2C, SPI, etc.) (ECLO-5)
6. Interrupts, ISRs, Concurrency (ECLO-6)
7. Sampling, A/D, and D/A conversion (precision, quantization, aliasing) (ECLO-7)
8. Elementary Control Theory (feedback, PID, etc.) (ECLO-8)

We'll be working all semester to build our skills and understanding in all these areas. However, **this** week's project focuses on DALO-1 (Estimating parameters), and ECLO-1 (Voltage Dividers, impedance).

Each week we'll be working on a project that will combine ideas from data analysis, programming, and electronics in the context of a laboratory experiment. Each project has a GitHub repository that contains most of what you need need for the that project. The repository is where you'll keep all your data, diagrams, simulations, and code.

There are some "in-class" components, some "in-lab" components, as well as some reading and homework you'll be doing over the same period.

* In Class: [Linear Regression (Curve Fitting)](CurveFitting.ipynb)
* In Lab: [Collecting Data from simple experiments](ControlAndMeasure.ipynb)
* Homework: Reading, Writing

As the semester progresses, the projects become less prescriptive and more open-ended. The final project is entirely open-ended.

Finally, these low level skills culminate in overall course outcomes that we'll be revisiting throughout the course:

clo-1 “Students can perform statistical analysis on data collected in the laboratory and make meaningful inferences, including estimates of confidence and uncertainty in model parameters derived from that data.” 

All of the projects will involve collecting data, processing that data, and drawing inferences of some kind.

clo-2 “Students will be able to design, construct and evaluate the performance of a variety of electrical circuits, including RC Circuits, PWM outputs, ADC and DAC-based interfaces, Serial (i2c, SPI, or rs232) interfaces, Operational Amplifiers, Filters, Triggers, and Digital Logic circuits of various kinds.” 

Each project involves building a circuit, testing, and making measurements.

clo-3 “Students will be able to write programs for microcontroller or PSoC interfaces to most, if not all, of these circuit types.”

Most of the projects involve writing code for a microcontroller to control the circuit and make measurements of circuit behavior.

clo-4 “Students will be able to design and implement an open-ended final project involving a computer-controlled interface to a circuit that solves an engineering problem or controls and monitors an external experiment.”

-----------------------

