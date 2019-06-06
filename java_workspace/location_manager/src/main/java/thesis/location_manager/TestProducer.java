package thesis.location_manager;


import java.sql.Timestamp;
import java.util.Date;
import java.util.concurrent.ExecutionException;

import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.clients.producer.RecordMetadata;

import com.google.gson.Gson;

/**
 * Hello world!
 *
 */
public class TestProducer
{
	@SuppressWarnings({ "rawtypes", "unchecked", "unused" })
	public static void main( String[] args )
	{
		Producer<Long, String> producer = ProducerCreator.createProducer();

		for (int index = 0; index < 100; index++) {
			
			
			
			Date date= new Date();
			Timestamp ts = new Timestamp(date.getTime());
			long latency = date.getTime();
			String tst = ts.toString();
			
			double orz = 0;
			double orx = 0;
			double ory = 0;
			double orw = 0;
			double posx = 0;
			double posy = 0;
			
			Goto go = new Goto(orx, ory, orz, orw, posx, posy, tst, latency);
			
			Gson gson = new Gson();
			String go_str = gson.toJson(go);
					
			ProducerRecord<Long, String> record = new ProducerRecord("turtle_goto" , go_str);

			try {
				RecordMetadata metadata = producer.send(record).get();

				System.out.println("Record sent with key " + index + " to partition " + metadata.partition()

				+ " with offset " + metadata.offset());

			} catch (InterruptedException e) {

				System.out.println("Error in sending record");
				System.out.println(e);

			} catch (ExecutionException e) {

				System.out.println("Error in sending record");
				System.out.println(e);

			}
			
			//Time.SYSTEM.sleep(1000);
			
			break;

		}
	}
}
