# Generated by Django 4.0.6 on 2022-07-24 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_firstdispute_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstdispute',
            name='value',
            field=models.CharField(choices=[('1', '01 О заключении, изменении и расторжении договоров'), ('2', '02 О недействительности сделок'), ('3', '03 О неисполнении или ненадлежащем исполнении обязательств по договорам'), ('4', '04 Внедоговорные обязательства'), ('5', '05 О проверке законности ненормативных актов, действий (бездействий) государственных органов, должностных лиц'), ('6', '06 О признании права собственности'), ('7', '07 Об истребовании имущества из чужого незаконного владения (виндикационный иск)'), ('8', '08 О нарушении прав, не связанных с лишением владения (негаторный иск)'), ('9', '09 О признании не подлежащим исполнению исполнительного документа, по которому взыскание производится в бесспорном порядке'), ('10', '10 О взыскании налогов, сборов, экономических санкций, других обязательных платежей в бюджет'), ('11', '11 О возврате из бюджета и государственных внебюджетных фондов денежных средств, списанных в бесспорном порядке'), ('12', '12 О ликвидации юридических лиц'), ('13', '13 О привлечении к субсидиарной ответственности'), ('14', '14 О прекращении деятельности индивидуальных предпринимателей'), ('15', '15 Об экономической несостоятельности (банкротстве)'), ('16', '16 О защите деловой репутации'), ('17', '17 Об установлении фактов, имеющих юридическое значение'), ('18', '18'), ('19', '19 По жалобам на нотариальные действия или отказ в их совершении'), ('20', '20 Нарушение законодательства об охране окружающей среды'), ('21', '21 Учредительство'), ('22', '22 О понуждении совершить определённые действия'), ('23', '23 Иные категории'), ('24', '24 Обжалование ответов на обращения юридических лиц, индивидуальных предпринимателей или граждан'), ('25', '25 О продлении приостановления (запрета) деятельности по заявлениям контролирующих органов'), ('26', '26 О приостановлении деятельности по заявлениям контролирующих органов'), ('27', '27 Споры в отношении находящегося в государственной собственности имущества'), ('28', '28 По жалобам на действия судебного исполнителя'), ('29', '29 О возбуждении приказного производства '), ('30', '30 О взыскании денежных средств'), ('31', '31 О выдаче исполнительного документа'), ('32', '32 О выдаче исполнительного документа на принудительное исполнение медиативного соглашения'), ('33', '33 О признании и приведении в исполнение решений иностранных судов на территории Республики Беларусь')], default='01 О заключении, изменении и расторжении договоров', max_length=122, verbose_name='Категория спора (подкатегория 1):'),
        ),
    ]
