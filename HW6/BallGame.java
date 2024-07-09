import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;

/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java, ShrinkBall.java, BounceBall.java, SplitBall.java, StdDraw.java
 *
 *  Creates and animates bouncing balls with player statistics.
 *******************************************************************************/

public class BallGame {

    public static void main(String[] args) {
        // Number of bouncing balls
        int numBalls = Integer.parseInt(args[0]);
        
        // Ball types and sizes
        String ballTypes[] = new String[numBalls];
        double ballSizes[] = new double[numBalls];
        
        int index = 1;
        for (int i = 0; i < numBalls; i++) {
            ballTypes[i] = args[index];
            ballSizes[i] = Double.parseDouble(args[index + 1]);
            index += 2;
        }

        // Create and initialize a player object for game statistics
        Player player = new Player();
        
        // Create a list to hold balls
        ArrayList<BasicBall> balls = new ArrayList<>();
        
        // Initialize the balls based on the given types and sizes
        for (int i = 0; i < numBalls; i++) {
            BasicBall newBall;
            switch (ballTypes[i].toLowerCase()) {
                case "basic":
                    newBall = new BasicBall(ballSizes[i], Color.RED);
                    break;
                case "shrink":
                    newBall = new ShrinkBall(ballSizes[i], Color.GREEN);
                    break;
                case "bounce":
                    newBall = new BounceBall(ballSizes[i], Color.BLUE);
                    break;
                case "split":
                    newBall = new SplitBall(ballSizes[i], Color.ORANGE);
                    break;
                default:
                    newBall = new BasicBall(ballSizes[i], Color.RED); // Fallback case
                    break;
            }
            balls.add(newBall);
        }

        // Number of active balls in the game
        int numBallsInGame = balls.size();
        
        // Set up the animation canvas
        StdDraw.enableDoubleBuffering();
        StdDraw.setCanvasSize(800, 800);
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);

        // Animation loop
        while (numBallsInGame > 0) {
            // Move all balls
            for (BasicBall ball : balls) {
                ball.move();
            }

            // Check if the mouse is clicked and a ball is hit
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                for (BasicBall ball : balls) {
                    if (ball.isHit(x, y) && !ball.isOut) { // Ensure ball is not already out
                        // randomizeSpeed(ball); // Randomize speed
                        ball.reset();
                        updatePlayerScore(player, ball); // Update player statistics
                    }
                }
            }

            // Reset the count of active balls
            numBallsInGame = 0;
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);

            // Draw balls and update active count
            for (BasicBall ball : balls) {
                if (!ball.isOut) {
                    ball.draw();
                    numBallsInGame++;
                }
            }

            // Print game progress and player statistics
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: " + numBallsInGame);
            StdDraw.text(-0.65, 0.80, "Hits: " + player.getHits());
            StdDraw.text(-0.65, 0.70, "Score: " + player.getScore());

            StdDraw.show();
            StdDraw.pause(20);
        }

        // Game over screen with final statistics
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");

            StdDraw.setFont(new Font("Arial", Font.BOLD, 20));
            StdDraw.text(0, -0.20, "Hits: " + player.getHits());
            StdDraw.text(0, -0.30, "Score: " + player.getScore());

            StdDraw.show();
            StdDraw.pause(10);
        }
    }
    
    // private static void randomizeSpeed(BasicBall ball) {
    //     double newSpeedX = (Math.random() - 0.5) * 0.02; // Random speed between -0.01 and 0.01
    //     double newSpeedY = (Math.random() - 0.5) * 0.02;
    //     ball.setSpeed(newSpeedX, newSpeedY);
    // }

    private static void updatePlayerScore(Player player, BasicBall ball) {
        switch (ball.getClass().getSimpleName()) {
            case "BasicBall":
                player.addScore(25);
                break;
            case "ShrinkBall":
                player.addScore(20);
                break;
            case "BounceBall":
                player.addScore(15);
                break;
            case "SplitBall":
                player.addScore(10);
                break;
        }
    }
}

// Player class for maintaining game statistics
class Player {
    private int score;
    private int hits;

    public Player() {
        this.score = 0;
        this.hits = 0;
    }

    public void addScore(int value) {
        this.score += value;
    }

    public void incrementHits() {
        this.hits++;
    }

    public int getScore() {
        return this.score;
    }

    public int getHits() {
        return this.hits;
    }
}
