# Java-Deserializer
This tool is responsible to perform java deserialization attacks on server end points

POC on Java De-Serialization vulnerability (Target: Any OS)
Pre-requiste: Download the ysoserial.jar file from https://github.com/frohoff/ysoserial and paste it in your project root directory of the attacker machine.

1) Prepare a maven project in your IDE and add the maven dependencies. 
2) On the victims machine, let us make use of the apache camel component jetty as our server end point. Start the application.

Snippet:
package POC_Serialization;

import javax.servlet.http.HttpSession;

import org.apache.camel.CamelContext;
import org.apache.camel.Exchange;
import org.apache.camel.Message;
import org.apache.camel.Processor;
import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.component.http.HttpMessage;
import org.apache.camel.impl.DefaultCamelContext;

public class POC_Test_Serialize {

	public static void main(String[] args) throws Exception {
		CamelContext context = new DefaultCamelContext();
		context.addRoutes(new RouteBuilder() {

			@Override
			public void configure() throws Exception {
				from("jetty:http://0.0.0.0:6060?")
				.process(new Processor() {

					@Override
					public void process(Exchange exchange) throws Exception {
						exchange.getIn().setBody("Response" + System.currentTimeMillis());
					}
				});	
			}
		});
		context.start();
	}

}
3) Open the terminal in the attacker machine and run the command python3 Serializer.py

References: Thanks to frohoff for the jar file.


