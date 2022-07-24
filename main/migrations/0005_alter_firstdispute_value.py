# Generated by Django 4.0.6 on 2022-07-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_firstdispute_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstdispute',
            name='value',
            field=models.CharField(choices=[('1 svdsvdsd', '01 О заключении, изменении и расторжении договоров'), ('2 csds', '02 О недействительности сделок'), ('3 scaszc', '03 О неисполнении или ненадлежащем исполнении обязательств по договорам'), ('4 s sccs', '04 Внедоговорные обязательства'), ('5 daca', '05 О проверке законности ненормативных актов, действий (бездействий) государственных органов, должностных лиц'), ('6 svsd', '06 О признании права собственности'), ('7 svd', '07 Об истребовании имущества из чужого незаконного владения (виндикационный иск)'), ('8 sced', '08 О нарушении прав, не связанных с лишением владения (негаторный иск)'), ('9 cs', '09 О признании не подлежащим исполнению исполнительного документа, по которому взыскание производится в бесспорном порядке'), ('10 vacs', '10 О взыскании налогов, сборов, экономических санкций, других обязательных платежей в бюджет'), ('11 sec', '11 О возврате из бюджета и государственных внебюджетных фондов денежных средств, списанных в бесспорном порядке'), ('12 vs', '12 О ликвидации юридических лиц'), ('13 vdsvds', '13 О привлечении к субсидиарной ответственности'), ('14sdc', '14 О прекращении деятельности индивидуальных предпринимателей'), ('15scd', '15 Об экономической несостоятельности (банкротстве)'), ('16dsc', '16 О защите деловой репутации'), ('17scd', '17 Об установлении фактов, имеющих юридическое значение'), ('18dc', '18'), ('19dsc', '19 По жалобам на нотариальные действия или отказ в их совершении'), ('20sdc', '20 Нарушение законодательства об охране окружающей среды'), ('21adetbtefe', '21 Учредительство'), ('22etrds', '22 О понуждении совершить определённые действия'), ('23dr', '23 Иные категории'), ('24adef', '24 Обжалование ответов на обращения юридических лиц, индивидуальных предпринимателей или граждан'), ('25edaf', '25 О продлении приостановления (запрета) деятельности по заявлениям контролирующих органов'), ('26efd', '26 О приостановлении деятельности по заявлениям контролирующих органов'), ('27 e ag', '27 Споры в отношении находящегося в государственной собственности имущества'), ('28earsgfer', '28 По жалобам на действия судебного исполнителя'), ('29aesbr', '29 О возбуждении приказного производства '), ('30ed', '30 О взыскании денежных средств'), ('31edr', '31 О выдаче исполнительного документа'), ('32aerd', '32 О выдаче исполнительного документа на принудительное исполнение медиативного соглашения'), ('33aertd', '33 О признании и приведении в исполнение решений иностранных судов на территории Республики Беларусь')], default='01 О заключении, изменении и расторжении договоров', max_length=122, verbose_name='Категория спора (подкатегория 1):'),
        ),
    ]
