package org.example;

public class Printer {

    private int numSheets;
    private int toner;

    public Printer(int numSheets, int toner){
        this.numSheets = numSheets;
        this.toner = toner;
    }

    public void print(int numSheetsToPrint, int numCopies){
        int totalSheets = numSheetsToPrint * numCopies;
        if (this.numSheets >= totalSheets && this.toner >= totalSheets) {
            this.numSheets -= totalSheets;
            this.toner     -= totalSheets;
        }
    }
    public int getNumSheets() {
        return this.numSheets;
    }

    public int getToner() {
        return this.toner;
    }
}
