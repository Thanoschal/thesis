package thesis.location_manager;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.concurrent.ExecutionException;

import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;

import com.fasterxml.jackson.databind.ObjectMapper;

public class LocationManager {

	@SuppressWarnings({ "deprecation", "rawtypes" })
	public static void main(String[] args) throws IOException, InterruptedException, ExecutionException {

		Producer<Long, String> producer = ProducerCreator.createProducer();
		Consumer<Long, String> consumer = ConsumerCreator.createConsumer("turtle_location");

		Scanner input = new Scanner(System.in);
		ObjectMapper mapper = new ObjectMapper();

		File experiment_A = new File("./resources/experiment_A");
		File experiment_B = new File("./resources/experiment_B"); 

		BufferedReader br_A = new BufferedReader(new FileReader(experiment_A)); 
		BufferedReader br_B = new BufferedReader(new FileReader(experiment_B)); 

		LinkedList<Goto> list_A = new LinkedList<Goto>();
		LinkedList<Goto> list_B = new LinkedList<Goto>();

		String point;

		System.out.println("Which experiment do you want to execute");
		System.out.println("1.Point-to-point.");
		System.out.println("2.Scaning of a room.");
		System.out.print("Give your choice: ");
		int choice = input.nextInt();

		String yn;

		if(choice == 1) {
			System.out.println("Experiment_A");

			while ((point = br_A.readLine()) != null) {
				Goto go = mapper.readValue(point, Goto.class);
				list_A.add(go);
			}


			for (int i = 0; i < list_A.size();) {
				System.out.print("Send the next point?(y/n): ");
				yn = input.next();

				if(yn.equals("y")) {
					
					Goto destination = list_A.get(i);
					String gotoJSON = mapper.writeValueAsString(destination);

					ProducerRecord<Long, String> record = new ProducerRecord<Long, String>("turtle_goto" , gotoJSON);
					producer.send(record);

					double distance = 10.0;
					
					while(distance > 0.1) {
						
						
						ConsumerRecords<Long, String> consumerRecords = consumer.poll(10);
						if (consumerRecords.count() == 0) {
							continue;
						}
						
						String loc = "";
						for(ConsumerRecord record1: consumerRecords) {
							loc = (String) record1.value();
						}
						
						Goto location = mapper.readValue(loc, Goto.class);
						
						distance = DistanceCalculation.distanceCalculation(location.getPosx(), location.getPosy(), destination.getPosx(), destination.getPosy());
						
						System.out.println("Robot is traveling... distance from goal: " + distance);

						consumer.commitAsync();


					}
					i++;
				}
				else {
					continue;
				}
				
				System.out.println("Robot reached the desired destination!!!!");
				
			}

		}
		else {
			System.out.println("Experiment_B");

			while ((point = br_B.readLine()) != null) {
				Goto go = mapper.readValue(point, Goto.class);
				list_B.add(go);
			}
			
			for (int i = 0; i < list_B.size();) {
				System.out.print("Send the next point?(y/n): ");
				yn = input.next();

				if(yn.equals("y")) {
					
					Goto destination = list_B.get(i);
					String gotoJSON = mapper.writeValueAsString(destination);

					ProducerRecord<Long, String> record = new ProducerRecord<Long, String>("turtle_goto" , gotoJSON);
					producer.send(record);

					double distance = 10.0;
					
					while(distance > 0.1) {
						
						
						ConsumerRecords<Long, String> consumerRecords = consumer.poll(10);
						if (consumerRecords.count() == 0) {
							continue;
						}
						
						String loc = "";
						for(ConsumerRecord record1: consumerRecords) {
							loc = (String) record1.value();
						}
						
						Goto location = mapper.readValue(loc, Goto.class);
						
						distance = DistanceCalculation.distanceCalculation(location.getPosx(), location.getPosy(), destination.getPosx(), destination.getPosy());
						
						System.out.println("Robot is traveling... distance from goal: " + distance);

						consumer.commitAsync();


					}
					i++;
				}
				else {
					continue;
				}
				
				System.out.println("Robot reached the desired destination!!!!");

			}
			
			
			
		}



		input.close();
		br_A.close();
		br_B.close();
		producer.close();
		consumer.close();


	} 

}

