import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import yahoofinance.Stock;
import yahoofinance.YahooFinance;

@SpringBootApplication
public class StockPriceApplication {

    public static void main(String[] args) {
        SpringApplication.run(StockPriceApplication.class, args);

        // Get the data for the stock NKLA
        Stock stock = YahooFinance.get("NKLA");

        // Get the current stock price
        double currentPrice = stock.getQuote().getPrice().doubleValue();

        // Display the current stock price
        System.out.printf("The current stock price of NKLA is $%.2f", currentPrice);
    }
}
