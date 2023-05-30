import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class RoomTest {

    Room room;

    @Before
    public void setUp() {
        room = new Room(4, 5, 6);
    }

    @Test
    public void canGetAreaFromParent(){
        assertEquals(20, room.getArea(), 0.01);
    }

    @Test
    public void canGetVolume() {
        assertEquals(120, room.getVolume(), 0.01);
    }
}
