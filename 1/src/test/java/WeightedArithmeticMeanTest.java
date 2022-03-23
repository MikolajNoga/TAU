import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.Set;

public class WeightedArithmeticMeanTest {
    private WeightedArithmeticMean average;
    private Set<WeightedNumber> numberSet;

    @BeforeEach
    public void setUp(){
        average = new WeightedArithmeticMean();
        numberSet = new HashSet<>();
    }

    @AfterEach
    public void tearDown(){
        average = null;
        numberSet = null;
    }

    @Test
    public void calculateAverageOnPositiveNumberValue(){
        numberSet.add(new WeightedNumber(5,5));
        numberSet.add(new WeightedNumber(10,10));
        numberSet.add(new WeightedNumber(1,1));

        double result = average.weightedArithmeticMean(numberSet);

        Assertions.assertEquals(7.875,result);
    }

    @Test
    public void calculateAverageOnNegativeNumberValue(){
        numberSet.add(new WeightedNumber(-5,5));
        numberSet.add(new WeightedNumber(-10,10));
        numberSet.add(new WeightedNumber(-1,1));

        double result = average.weightedArithmeticMean(numberSet);

        Assertions.assertEquals(-7.875,result);
    }

    @Test
    public void calculateAverageOnNegativeNumberWeight(){
        numberSet.add(new WeightedNumber(5,-5));
        numberSet.add(new WeightedNumber(10,10));
        numberSet.add(new WeightedNumber(1,1));

        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            double result = average.weightedArithmeticMean(numberSet);
        });
    }

    @Test
    public void calculateAverageWhenProvidedSetWith0WeightValue(){
        numberSet.add(new WeightedNumber(5,0));
        numberSet.add(new WeightedNumber(10,1));
        numberSet.add(new WeightedNumber(1,1));

        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            double result = average.weightedArithmeticMean(numberSet);
        });
    }

    @Test
    public void calculateAverageWithEmptySet(){
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            double result = average.weightedArithmeticMean(numberSet);
        });
    }

    @Test
    public void weightedNumberGettersShouldReturnProvidedValues(){
        WeightedNumber number = new WeightedNumber(1,5);
        Assertions.assertEquals(number.getWeight(), 5.0);
        Assertions.assertEquals(number.getNumber(), 1.0);
    }

    @Test
    public void weightedNumberSetNumberShouldUpdateNewValue(){
        WeightedNumber number = new WeightedNumber(1,5);
        number.setNumber(100);
        Assertions.assertEquals(number.getNumber(), 100.0);
    }

    @Test
    public void weightedNumberSetWeightShouldUpdateNewValue(){
        WeightedNumber number = new WeightedNumber(1,5);
        number.setWeight(100);
        Assertions.assertEquals(number.getWeight(), 100.0);
    }
}
