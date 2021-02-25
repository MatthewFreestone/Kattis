import java.util.*;

public class air{
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		Minion[] minions = new Minion[n];
		for(int i = 0; i < n; i++){
			minions[i] = new Minion(in.nextInt(), in.nextInt());
		}

		List<Room> rooms = new ArrayList<Room>();
		rooms.add(new Room(minions[0].min, minions[0].max));
		for (int i = 1; i < n; i++) {
			boolean foundRoom = false;
			for (Room r: rooms){
				if (minions[i].canBeInRoom(r)){
					//System.out.println(r);
					foundRoom = true;
					r.newMinion(minions[i]);
					break;
				}
			}
			if (!foundRoom){
				rooms.add(new Room(minions[i].min, minions[i].max));
			}
		}
		System.out.println(rooms.size());
	}
}

class Minion{
	public int min;
	public int max; 
	public Minion(int min, int max){
		this.min = min;
		this.max = max;
	}

	public boolean canBeInRoom(Room room){
		if (room.max >= this.min || room.min >= this.max){
			return true;
		}
		return false; 
	}

}

class Room{
	public int min;
	public int max;
	public Room(int min, int max){
		this.min = min;
		this.max = max;
	}
	public void newMinion(Minion m){
		int min_other = m.min;
		int max_other = m.max;
		min = (min_other > min) ? min_other : min;
		max = (max_other < max) ? max_other : max;
	}
	@Override
	public String toString() {
		return "Room is Min: " + min + ", Max: " + max;
	}
}

