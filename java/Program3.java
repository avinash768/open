import java.util.HashSet;
import java.util.Set;

public class Program3 {
    public static boolean isPangram(String s) {
        s = s.toLowerCase();
        Set<Character> letters = new HashSet<>();

        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                letters.add(c);
            }
        }

        return letters.size() == 26;
    }

    public static void main(String[] args) {
        System.out.println(isPangram("The quick brown fox jumps over the lazy dog."));
        System.out.println(isPangram("This is not a pangram."));
    }
}
