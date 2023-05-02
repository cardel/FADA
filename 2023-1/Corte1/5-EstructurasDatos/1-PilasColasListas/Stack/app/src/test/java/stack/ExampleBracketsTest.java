package stack;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class ExampleBracketsTest {

    @Test
    void solve() {
        String test1 = "([<{abc123abc}>])";
        String test2 = "(abc[123)abc]";

        ExampleBrackets objExampleBrackets = new ExampleBrackets();
        assertTrue(objExampleBrackets.solve(test1));
        assertFalse(objExampleBrackets.solve(test2));
    }
}