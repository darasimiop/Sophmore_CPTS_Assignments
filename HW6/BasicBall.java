import java.awt.Color;


public class BasicBall {
    protected double rx, ry; // Position
    protected double vx, vy; // Velocity
    protected double radius; // Radius
    protected final Color color; // Color
    public boolean isOut;

    // Constructor
    public BasicBall(double r, Color c) {
        this.rx = 0.0;
        this.ry = 0.0;
        randomizeSpeed();
        this.radius = r;
        this.color = c;
        this.isOut = false;
    }

    public void randomizeSpeed() {
        double minSpeed = -0.01; // minimum speed
        double maxSpeed = 0.01; // maximum speed
    
        this.vx = StdRandom.uniform(minSpeed, maxSpeed); // Random speed in x direction
        this.vy = StdRandom.uniform(minSpeed, maxSpeed); // Random speed in y direction
    }
    

    // Move the ball one step
    public void move() {
        this.rx += this.vx;
        this.ry += this.vy;
        if (isOutOfBound()) {
            this.isOut = true;
        }
    }

    // Check if the ball is out of bounds
    private boolean isOutOfBound() {
        return Math.abs(this.rx) > 1.0 || Math.abs(this.ry) > 1.0;
    }

    // Draw the ball
    public void draw() {
        if (!this.isOut) {
            StdDraw.setPenColor(this.color);
            StdDraw.filledCircle(this.rx, this.ry, this.radius);
        }
    }

    public void reset() {
        this.rx = 0.0;
        this.ry = 0.0;
        randomizeSpeed();
        this.isOut = false;
    }

    public boolean isHit(double x, double y) {
        return Math.abs(this.rx - x) <= this.radius && Math.abs(this.ry - y) <= this.radius;
    }

    public int getScore() {
        return 25; // Default score for a basic ball
    }

    public double getRadius() {
        return this.radius;
    }
}

class ShrinkBall extends BasicBall {
    private final double originalRadius;

    public ShrinkBall(double r, Color c) {
        super(r, c);
        this.originalRadius = r; // Save the original radius
    }

    // @Override
    // public void move() {
    //     super.move();

    //     if (this.radius <= originalRadius * 0.25) { // Reset when it reaches 25% or less
    //         reset();
    //     } else {
    //         this.radius *= 0.67; // Continue shrinking
    //     }
    // }

    @Override
    public void reset() {
        super.reset();
        // Reset to original size
        if (this.radius <= originalRadius * 0.25) { // Reset when it reaches 25% or less
            this.radius = originalRadius;
                } else {
                    this.radius *= 0.67; // Continue shrinking
                }
    }

    @Override
    public int getScore() {
        return 20; // Score for hitting a ShrinkBall
    }
}


class BounceBall extends BasicBall {
    private int bounceCount;

    public BounceBall(double r, Color c) {
        super(r, c);
        this.bounceCount = 4; // Allow three bounces before it exits
    }

    @Override
    public void move() {

        if (bounceCount <= 0) {
            this.isOut = true; // Mark the ball as out when bounce count is zero
        }

        this.rx += this.vx;
        this.ry += this.vy;

        if (Math.abs(this.rx) > 1.0) {
            this.vx = -this.vx; // Reverse x-velocity on bounce
            bounceCount--; // Decrement bounce count
        }

        if (Math.abs(this.ry) > 1.0) {
            this.vy = -this.vy; // Reverse y-velocity on bounce
            bounceCount--; // Decrement bounce count
        }

        
    }

    @Override
    public int getScore() {
        return 15; // Score for hitting a BounceBall
    }
}


class SplitBall extends BasicBall {
    public SplitBall(double r, Color c) {
        super(r, c);
    }

    public BasicBall[] split() {
        BasicBall[] newBalls = new BasicBall[2];
        newBalls[0] = new SplitBall(this.radius, this.color); // Create new split balls
        newBalls[1] = new SplitBall(this.radius, this.color);

        newBalls[0].reset(); // Reset position to center with random speed
        newBalls[1].reset();

        return newBalls;
    }

    @Override
    public int getScore() {
        return 10; // Score for hitting a SplitBall
    }
}
