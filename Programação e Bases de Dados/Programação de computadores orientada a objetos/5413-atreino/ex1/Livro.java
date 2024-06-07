public class Livro{

    public Livro(String titulo, String autor, int anoPub, Boolean disponibilidade){
        setAnoPub(anoPub);
        setAutor(autor);
        setDisponibilidade(disponibilidade);
        setTitulo(titulo);
    }

    //Atributos
    private String titulo;
    private String autor;
    private int anoPub;
    private Boolean disponibilidade;

    //Getters e Setters

    public String getTitulo() {
        return this.titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return this.autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getAnoPub() {
        return this.anoPub;
    }

    public void setAnoPub(int anoPub) {
        this.anoPub = anoPub;
    }

    public Boolean isDisponibilidade() {
        return this.disponibilidade;
    }

    public Boolean getDisponibilidade() {
        return this.disponibilidade;
    }

    public void setDisponibilidade(Boolean disponibilidade) {
        this.disponibilidade = disponibilidade;
    }

    //Métodos
    
    public void emprestar(){
        this.disponibilidade = false;
    }

    public void devolver(){
        this.disponibilidade = true;
    }

    public void exibirDetalhes(){
        System.out.println("Livro: " + this.titulo + "\n" +
        "autor: "+this.autor+"\n"+"Ano Publicação: "+this.anoPub+"\n"+"Disponivel: "+this.disponibilidade);
    }


}