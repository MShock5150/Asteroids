# Asteroids - A Python OOP Project

## Project Overview

This project is a recreation of the classic arcade game "Asteroids," built entirely in Python using the `pygame` library. The primary goal of this project was to gain practical experience with **Object-Oriented Programming (OOP)** principles. By modeling each game element as a distinct object, the project demonstrates a clear and organized approach to game development.

Players control a spaceship in a 2D environment, tasked with destroying asteroids while avoiding collisions.

## Key Features & Design

* **Object-Oriented Architecture:** Every element in the game is an object, demonstrating a clear separation of concerns.
    * `Spaceship`: Manages player movement, rotation, shooting, and collision detection.
    * `Asteroid`: Handles its own movement, size, and the logic for splitting into smaller asteroids when destroyed.
    * `Bullet`: Manages its own trajectory and lifespan.
* **Classic Game Mechanics:**
    * Responsive player controls for rotation and thrust.
    * Screen-wrapping for all game objects.
    * Progressive difficulty as smaller, faster asteroids are spawned.
* **Vector-Based Graphics:** Utilizes simple geometric shapes to replicate the look and feel of the original vector-based arcade game.

## How to Run

To play the game, you first need to install the `pygame` library.

1.  **Install Pygame:**
    ```bash
    pip install pygame
    ```
2.  **Run the Game:**
    From the root of the project directory, run the main script:
    ```bash
    python3 src/main.py
    ```

## Controls

* **Rotate Left:** `Left Arrow`
* **Rotate Right:** `Right Arrow`
* **Thrust Forward:** `Up Arrow`
* **Shoot:** `Spacebar`

---

*This project was built as part of the backend development curriculum on [Boot.dev](https://www.boot.dev) to practice Object-Oriented Programming concepts.*
