package org.example;

import java.util.ArrayList;

public class Main {
    public static int findNeedle(String[] hayStack){
        boolean found = false;
        int position = 0;
        while (found == false){
            if (hayStack[position] == "needle"){
                found = true;
                return position;

            } else {
                position ++;
            }
        }
        return -1;
    }
    public static int countHay(String[] hayStack) {
        int hayAmount = 0;
        for (String mightBeHay : hayStack) {
            if (mightBeHay == "hay") {
                hayAmount ++;
            }
        }
        return hayAmount;
    }
    public static void main(String[] args) {
        String[]  hayStack = {"hay", "hay", "hay", "needle", "hay", "hay"};
        System.out.println("The needle was found in position " + findNeedle(hayStack));
        System.out.println("I found " + countHay(hayStack) + " pieces of hay");
    }
}
