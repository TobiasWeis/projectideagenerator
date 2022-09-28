#!/usr/bin/python3
'''
author: Tobias Weis

This program generates project ideas from building blocks, for example:

    - [mobile application] that [helps to find] [devs]

In a first step, these blocks will be sampled from pre-populated lists
'''

import sys,os
import random
import numpy as np
import matplotlib.pyplot as plt

def populate_list(fname):
    lines = open(fname,"r").readlines()
    rc = []
    for l in lines:
        rc.append(l.rstrip())
    return rc

industries = populate_list("data/list_industries.txt")

actor = [
        "Mobile app",
        "Desktop application",
        "Program",
        "Wearable",
        "GUI",
        "API",
        "Device",
        "Robot",
        "Microcontroller",
        "Location-based social network",
        "Subscription model",
        "Digital assistant",
        "Consultancy",
        "Product"
        ]

action = [
        "helps to find",
        "matches",
        "calculates",
        "scrapes",
        "simulates",
        "visualizes",
        "computes",
        "saves",
        "supports",
        "lists",
        "creates",
        "connects",
        "scales",
        "identifies",
        "finds",
        "eliminates",
        "rates",
        "scores",
        "educates",
        "serves",
        "measures",
        "reduces",
        "improves",
        "generates",
        "designs",
        "tracks",
        "verifies",
        "automates",
        "consults",
        "repairs",
        "detects",
        "buys",
        "sells",
        "monitors"
        ]

acted_on = [
        "developers",
        "managers",
        "spreadsheets",
        "marketing-triggers",
        "energy",
        "heating",
        "resources",
        "cars",
        "mobile phones",
        "bank accounts",
        "domains",
        "plattforms",
        "servers",
        "recommendations",
        "bookings",
        "alerts",
        "ratings",
        "content",
        "infrastructure",
        "KPIs",
        "risks",
        "robots",
        "source code",
        "acceptance",
        "usage",
        "health information",
        "loans",
        "authenticity",
        "luxury estates",
        "luxury goods",
        "rare items",
        "accomodation",
        "transport",
        "vitamins",
        "stocks",
        "remote-work",
        "vacations",
        "habits",
        "photos",
        "thermostats",
        "smartphones",
        "recruiting",
        "financial services",
        "shopping",
        "repairs",
        "fundraising",
        "customer service",
        "data",
        "documents",
        "photos",
        "medical procedures",
        "expenses",
        "campaigns"
        ]

by_using = [
        "AI",
        "IoT",
        "Blockchain",
        "NLP",
        "Simulations",
        "Adaptive Technology",
        "Agile development",
        "Big Data",
        "Business Intelligence",
        "Cloud Computing",
        "Crowd Sourcing",
        "Green technology",
        "Wearables",
        "Biometrics",
        "API",
        "The Internet",
        "Augmented Reality",
        "Computer Vision",
        "Middleware",
        "Gamification",
        "Custom Electronics",
        "3D Printing",
        "CI/CD",
        "Distributed Systems",
        "Service",
        "Datadriven Customer-Support",
        "Text-To-Speech",
        "OCR",
        "Smartphones",
        "GPS data",
        "Digital Diary",
        "Live Feed",
        "Scoring system",
        "Cellular network"
        ]

def get(arr):
    return random.sample(arr,1)[0]

def main():
    for i in range(10):
        print(f"- {get(actor)} that {get(action)} {get(acted_on)} by using {get(by_using)} (in the industry of {get(industries)})") 

if __name__ == "__main__":
    main()

