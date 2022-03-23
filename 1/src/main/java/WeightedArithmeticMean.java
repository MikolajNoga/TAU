import java.util.Set;

public class WeightedArithmeticMean {
    public double weightedArithmeticMean(Set<WeightedNumber> numberSet){
        if (numberSet.isEmpty())
            throw new IllegalArgumentException();

        double result = 0.0;
        int divider = 0;

        for (WeightedNumber number: numberSet) {
            if (number.getWeight() <= 0)
                throw new IllegalArgumentException();
            result += number.getNumber() * number.getWeight();
            divider += number.getWeight();
        }

        result /= divider;

        return result;
    }
}
