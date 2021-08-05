package utp.misiontic2022.c2.p47.unidad4_5.modelo.vo;

public class Stock {
    private int id_book;
    private int amount;

    public Stock() {
    }

    public Stock(int id_book, int amount) {
        this.id_book = id_book;
        this.amount = amount;
    }

    public int getId_book() {
        return id_book;
    }

    public void setId_book(int id_book) {
        this.id_book = id_book;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
}
