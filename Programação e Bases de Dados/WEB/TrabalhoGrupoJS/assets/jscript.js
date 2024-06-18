$(function() {
    var events = [
        { year: 1969, text: "1969: A ARPANET, precursora da internet, faz sua primeira conexão entre universidades nos EUA." },
        { year: 1983, text: "1983: O protocolo TCP/IP é introduzido, formando a base da internet moderna." },
        { year: 1991, text: "1991: Tim Berners-Lee lança a World Wide Web." },
        { year: 1998, text: "1998: Google é fundado, revolucionando a busca na internet." },
        { year: 2004, text: "2004: Facebook é lançado, marcando o início das redes sociais como as conhecemos." },
        { year: 2007, text: "2007: O iPhone é lançado, impulsionando a era dos smartphones e da internet móvel." },
        { year: 2010, text: "2010: Instagram é lançado, popularizando o compartilhamento de fotos." },
        { year: 2015, text: "2015: O conceito de Internet das Coisas (IoT) começa a ganhar popularidade." },
        { year: 2020, text: "2020: A pandemia de COVID-19 acelera a adoção de tecnologias digitais." }
    ];

    $("#slider").slider({
        min: 0,
        max: events.length - 1,
        step: 1,
        slide: function(event, ui) {
            $("#event-text").text(events[ui.value].text);
        }
    });

    // Initialize with the first event
    $("#event-text").text(events[0].text);
});
