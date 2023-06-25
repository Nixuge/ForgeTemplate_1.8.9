package <MODPACKAGE>.<MODID>;

import lombok.Getter;
import lombok.Setter;
import net.minecraftforge.fml.common.Mod;

@Mod(
        modid = McMod.MOD_ID,
        name = McMod.NAME,
        version = McMod.VERSION,
        clientSideOnly = true
)

@Setter
public class McMod {
    public static final String MOD_ID = "<MODID>";
    public static final String NAME = "<MODNAME>";
    public static final String VERSION = "<MODVERSION>";


    @Getter
    @Mod.Instance(value = McMod.MOD_ID)
    private static McMod instance;
}
