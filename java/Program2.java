import java.util.HashMap;
import java.util.Map;

public class Program2 {
    private static final Map<Character, Integer> ROMAN_NUMERAL_VALUES = new HashMap<>();

    static {
        ROMAN_NUMERAL_VALUES.put('I', 1);
        ROMAN_NUMERAL_VALUES.put('V', 5);
        ROMAN_NUMERAL_VALUES.put('X', 10);
        ROMAN_NUMERAL_VALUES.put('L', 50);
        ROMAN_NUMERAL_VALUES.put('C', 100);
        ROMAN_NUMERAL_VALUES.put('D', 500);
        ROMAN_NUMERAL_VALUES.put('M', 1000);
    }

    public static int romanToInt(String s) {
        int sum = 0;
        int prev = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            int current = ROMAN_NUMERAL_VALUES.get(s.charAt(i));
            if (current < prev) {
                sum -= current;
            } else {
                sum += current;
            }
            prev = current;
        }

        return sum;
    }

    public static void main(String[] args) {
        System.out.println(romanToInt("IX"));
       
    }
}
