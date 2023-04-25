package stack;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class ChallengeExerciseTest {

    @Test
    void solve() {
        ChallengeExercise objChallenge = new ChallengeExercise();
        assertTrue(objChallenge.solve("([<{abc123abc}>])"));
        assertFalse(objChallenge.solve("(abc[123)abc]"));
    }
}