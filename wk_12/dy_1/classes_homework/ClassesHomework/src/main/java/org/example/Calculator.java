package org.example;

public class Calculator {

    public Calculator() {}

    public int add(int val1, int val2){
        return val1 + val2;
    }

    public int subtract(int val1, int val2){
        return val1 - val2;
    }

    public int multiply(int val1, int val2){
        return val1 * val2;
    }

    public double divide(double val1, double val2){
        return val1 / val2;
    }
}


//Calculator
//        Create a Calculator class.
//        This should have functions for Add, Subtract, Multiply and Divide.
//        Your methods should take in two ints to perform the calculations on (except the Divide method. This should take two doubles as arguments).
//        HINT: you will need to have an empty constructor function or no constructor function at all!(The compiler automatically provides a public no-argument constructor for any class without constructor)