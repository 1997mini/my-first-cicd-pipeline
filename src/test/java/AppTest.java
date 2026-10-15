import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AppTest {

    @Test
    public void testMathLogic() {
        int expected = 30;
        int actual = 10 + 20;

        System.out.println("Executing automated Java unit test...");
        assertEquals(expected, actual, "Math calculation should match!");
    }
}
