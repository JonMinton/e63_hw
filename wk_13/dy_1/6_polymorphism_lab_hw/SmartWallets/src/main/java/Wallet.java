import java.lang.reflect.Array;
import java.util.ArrayList;

public class Wallet {

    private ArrayList<IChargeable> chargeables;
    private IChargeable activeChargeable;

    public Wallet() {
        this.chargeables = new ArrayList<>();
    }

    public void addChargeable(IChargeable chargeable){
        this.chargeables.add(chargeable);
    }

    public void selectActiveChargeable(IChargeable chargeable){
        if (this.chargeables.contains(chargeable)){
            this.activeChargeable = chargeable;
        }
    }

    public void chargeWithActive(double amount){
        if (this.activeChargeable != null) {
            this.activeChargeable.charge(amount);
        }
    }

    public int getNumChargeables() {
        return this.chargeables.size();
    }


}
